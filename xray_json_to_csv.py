#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
@version: 0.1
@author: thatqier
@contact: 11875409@qq.com
@site: 1
@file: xray.py
@time: 2019/8/15 11:54 PM
"""

import json
import time
import csv

def zhuanhuan(json_file,save_file):
    wb = 0
    dqr = 0
    csvfile = open(save_file, "w+")
    writer = csv.writer(csvfile)
    writer.writerow(('create_time','expected_value','filename','header_name','header_value','host','param','payload','plugin','port','request','request1','request2','response','response1','response2','target','title','type','url','vuln_class','判定'))

    with open(json_file,'r') as load_f:
        load_dict = json.load(load_f)
        for i in range(0,len(load_dict)):
            mate = ''
            try:
                #时间戳转换成了时间，不需要的话可以去掉
                create_time = time_zh(load_dict[i]['create_time'])
            except:
                create_time = ''
            try:
                expected_value = load_dict[i]['detail']['expected_value']
            except:
                expected_value = ''
            try:
                header_name = load_dict[i]['detail']['header_name']
            except:
                header_name = ''
            try:
                header_value = load_dict[i]['detail']['header_value']
            except:
                header_value = ''
            try:
                filename = load_dict[i]['detail']['filename']
            except:
                filename = ''
            try:
                host = load_dict[i]['detail']['host']
            except:
                host = ''
            try:
                param = load_dict[i]['detail']['param']
            except:
                param =''
            try:
                payload = load_dict[i]['detail']['payload']
            except:
                payload =''
            try:
                port = load_dict[i]['detail']['port']
            except:
                port = ''
            try:
                request = load_dict[i]['detail']['request']
            except:
                request = ''
            try:
                request1 = load_dict[i]['detail']['request1']
            except:
                request1 = ''
            try:
                request2 = load_dict[i]['detail']['request2']
            except:
                request2 = ''
            try:
                response = load_dict[i]['detail']['response']
                mate = wubao_pa(response,mate)
            except:
                response = ''
            try:
                response1= load_dict[i]['detail']['response1']
                mate = wubao_pa(response1,mate)
            except:
                response1 = ''
            try:
                response2= load_dict[i]['detail']['response2']
                mate =wubao_pa(response2,mate)
            except:
                response2 = ''
            try:
                title = load_dict[i]['detail']['title']
                mate = wubao_pa(title,mate)
            except:
                title = ''
            try:
                type = load_dict[i]['detail']['type']
            except:
                type = ''
            try:
                url = load_dict[i]['detail']['url']
            except:
                url = ''
            try:
                plugin = load_dict[i]['plugin']
            except:
                plugin = ''
            try:
                target = load_dict[i]['target']['url']
            except:
                target = ''
            try:
                vuln_class = load_dict[i]['vuln_class']
            except:
                vuln_class = ''
            if(mate ==''):
                mate = "待确认"
                dqr = dqr + 1
            else:
                wb = wb +1
            writer.writerow((create_time,expected_value,filename,header_name,header_value,host,param,payload,plugin,port,request,request1,request2,response,response1,response2,target,title,type,url,vuln_class,mate))
            #print(create_time,expected_value,header_name,header_value,host,param,payload,port,request,plugin)
        print("本次扫描共有" + str(len(load_dict)) + "条结果，其中需要确认的："  + str(dqr) + "条，疑似误报："+ str(wb) + ",请处理" )
    csvfile.close()

def wubao_pa(word,mate):
    #误报关键字名单
    black_list = ['waf','WAF','防火墙','拦截','频繁','攻击','阻止','非法']
    for list in black_list:
        if(list in word):
            mate = mate + list
    return mate

def time_zh(timeNum):
    timeStamp = float(timeNum / 1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

if __name__ == '__main__':
    #result_qq.json为生成的文件
    #1.csv为要保存的文档
    zhuanhuan("result_qq.json","1.csv")