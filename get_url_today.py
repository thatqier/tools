#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
@version: 0.1
@author: thatqier
@contact: 11875409@qq.com
@site: 1
@software: PyCharm
@file: get_url_today.py
@time: 2019/8/2 12:07 AM
根据overlin的excel表来进行域名数据提取
"""
import time
import xlrd

worksheet = xlrd.open_workbook('1.xls')
sheet_names = worksheet.sheet_names()
for i in range(0,len(sheet_names)):
    sheet_na = sheet_names[i]
    sheet2 = worksheet.sheet_by_name(sheet_na)
    rows = sheet2.nrows
    for id in range(1,rows):
        rows = sheet2.row_values(id)
        url = rows[1]
        datatime = rows[5]
        timeArray = time.strptime(datatime, "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(timeArray))
        hang = hang + 1
        now_time = int(time.time())
        if(now_time - timeStamp < 259200):
            print(url)


