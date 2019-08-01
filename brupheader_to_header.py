#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
@version: 0.1
@author: thatqier
@contact: 11875409@qq.com
@site: 1
@software: PyCharm
@file: brupheader_to_header.py
@time: 2019/8/1 10:22 AM
主要是用来把brup中的头文件进行转化
"""

def zhuanhuan(header):
    test = '''
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0
    Accept: application/json, text/javascript, */*; q=0.01
    Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
    Accept-Encoding: gzip, deflate
    Referer: wwww
    Content-Type: application/x-www-form-urlencoded; charset=UTF-8
    X-Requested-With: XMLHttpRequest
    '''
    header = header.split('\n')
    result = ""
    for i in range(0,len(header)):
        chang = header[i]
        if(":" in chang):
            chang = chang.replace(' ','')
            ge = chang.split(':')
            for m in range(0,1):
                result_l = '\'' + ge[0] + '\''
                result_m = '\'' + ge[1] + '\''
            gai = result_l + ':' + result_m
            result = result  + gai + "\n"
    return result


if __name__ == '__main__':
    resulr = zhuanhuan('''
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0
    Accept: application/json, text/javascript, */*; q=0.01
    Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
    Accept-Encoding: gzip, deflate
    Referer: http://ld.ldfaka.com/links/ECAC0DADFF37B100
    Content-Type: application/x-www-form-urlencoded; charset=UTF-8
    X-Requested-With: XMLHttpRequest
    
    ''')
    print(resulr)