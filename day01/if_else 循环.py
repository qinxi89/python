#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2019/12/11 9:56 下午
# @Author  : qinxi
# @Site    : www.iqinxi.com
# @File    : test.py

##################################################################
#场景一：判断分数
score = int(input("请输入一个分数："))
if 100 >=  score >= 90:
    print('A')
elif 90 > score >=  80:
    print('B')
elif 80 >  score >= 60:
    print('C')
elif 60 > score >= 0:
    print('D')
else:
    print('输入错误！')

##################################################################
#场景二：用户登录验证
# 提示输入用户名和密码
# 验证用户名和密码
#     如果错误，则输出用户名或密码错误
#     如果成功，则输出 欢迎，XXX!
    
import getpass

name = input('please input you name:')
pwd = getpass.getpass('please input you sercert:')
if name == 'qinxi' and pwd == 'cuihua':
    print("welcome ,qinxi!")
else:
    print("you name or sercert is error ！")
##################################################################
    
    
    
    
    
    
