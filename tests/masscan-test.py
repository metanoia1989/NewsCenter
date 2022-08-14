#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import masscan

mas = masscan.PortScanner()

mas.scan('192.168.0.0/16', ports='22,80,8080', arguments='--max-rate 1000')
print(mas.scan_result)