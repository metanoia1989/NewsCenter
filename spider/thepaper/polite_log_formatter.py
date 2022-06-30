#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'youmi'
from scrapy import logformatter
import logging

#http://qubanshi.cc/questions/1330035/scrapy-silently-drop-an-item
class PoliteLogFormatter(logformatter.LogFormatter):
    def dropped(self, item, exception, response, spider):
        return {
            'level': logging.DEBUG,
            'msg': logformatter.DROPPEDMSG,
            'args': {
                'exception': exception,
                'item': item,
            }
        }
