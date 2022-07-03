#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
贴吧爬虫 主要爬取隐居吧 龙华吧  
爬取只要第一楼，回复不抓取，每3个小时更新一次    
写一个通用的贴吧爬虫，不同的吧传入吧名即可    
"""

from base64 import encode
from copyreg import constructor
from requests import request
import scrapy
import json
import time
from math import ceil
from thepaper.items import NewsItem
from thepaper.utils import helper
from urllib.parse import quote

class TiebaSpider(scrapy.Spider):
    name = "tieba"
    cur_page = 1    #modified by pipelines (open_spider)
    end_page = 50 
    filter = None
    see_lz = False
    tbname = '龙华'

    # 吧名必须编码，不然就拿不到内容，满离谱的哈哈 
    page_url = "https://tieba.baidu.com/f?kw=" + quote(tbname) + "&pn={pn}"
    start_urls =[
        page_url.format(pn = (cur_page - 1)*50)
    ]


    def parse(self, response): #forum parser
        print(("Crawling page %d..." % self.cur_page))
        print("请求地址啊", response.url, response.meta)

        for sel in response.xpath('//li[contains(@class, "j_thread_list")]'):
            data = json.loads(sel.xpath('@data-field').get())
            print('数据啊', data)
            if data['id'] == 1: # 去掉"本吧吧主火热招募"
                continue
            item = {}
            item['id'] = data['id']
            item['author'] = data['author_name']
            item['reply_num'] = data['reply_num']
            item['good'] = data['is_good']
            if not item['good']:
                item['good'] = False
            item['title'] = sel.xpath('.//div[contains(@class, "threadlist_title")]/a/@title').extract_first()
            if self.filter and not self.filter(item["id"], item["title"], item['author'], item['reply_num'], item['good']):
                continue
            #filter过滤掉的帖子及其回复均不存入数据库
                
            url = 'http://tieba.baidu.com/p/%d' % data['id']
            if self.see_lz:
                url += '?see_lz=1'
            meta = {'thread_id': data['id'], 'page': 1, 'thread': item, 'url': url}
            yield scrapy.Request(url, callback = self.parse_post,  meta = meta)

        next_page = response.xpath('//a[@class="next pagination-item "]/@href')
        self.cur_page += 1
        if next_page:
            if self.cur_page <= self.end_page:
                yield scrapy.Request('http:'+next_page.extract_first())
            
    def parse_post(self, response): 
        meta = response.meta
        for floor in response.xpath("//div[contains(@class, 'l_post')]"):
            if not helper.is_ad(floor):
                data = json.loads(floor.xpath("@data-field").extract_first())
                item = NewsItem()

                item['news_url'] = data['thread']['url']
                item['title'] = meta['thread']['title']
                item['author'] = meta['thread']['author']
                content = floor.xpath(".//div[contains(@class,'j_d_post_content')]").extract_first()
                #以前的帖子, data-field里面没有content
                item['content'] = helper.parse_content(content)
                #以前的帖子, data-field里面没有thread_id
                item['thread_id'] = meta['thread_id']
                item['floor'] = data['content']['post_no']
                #只有以前的帖子, data-field里面才有date
                if 'date' in list(data['content'].keys()):
                    item['news_date'] = data['content']['date']
                    #只有以前的帖子, data-field里面才有date
                else:
                    item['news_date'] = floor.xpath(".//span[@class='tail-info']")\
                    .re_first(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}')
                item['crawl_date'] = helper.today()
                yield item
                break

        next_page = response.xpath(".//ul[@class='l_posts_num']//a[text()='下一页']/@href")
        if next_page:
            meta['page'] += 1
            url = response.urljoin(next_page.extract_first())
            yield scrapy.Request(url, callback = self.parse_post, meta = meta, 
                headers=self.my_headers)
