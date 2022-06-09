#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Python中获取当前日期的格式 https://www.cnblogs.com/wenblog/p/6023742.html   
"""

import datetime
import time
i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)


print (time.strftime("%Y-%m-%d %H:%M:%S"))