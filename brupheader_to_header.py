#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
@version: 0.2
@author: thatqier
@contact: 11875409@qq.com
@site: 1
@software: PyCharm
@file: brupheader_to_header.py
@time: 2019/8/1 10:22 AM
主要是用来把brup中的头文件进行转化
"""

def zhuanhuan(header):
    header = header.split('\n')
    result = ""
    for i in range(0,len(header)):
        chang = header[i]
        if(":" in chang):
            chang = chang.replace(' ','')
            ge = chang.split(':')
            result_l = '\'' + ge[0] + '\''
            result_m = '\''
            for m in range(1,len(ge)):
                result_m = result_m +str(ge[m])+':'
            result_m = result_m[:-1]  + '\''
            gai = result_l + ':' + result_m
            result = result  + gai + ",\n"
    return result


if __name__ == '__main__':
    resulr = zhuanhuan('''''')
    print(resulr)