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
 场景二、猜年龄游戏
在程序里设定好你的年龄，然后启动程序让用户猜测，用户输入后，根据他的输入提示用户输入的是否正确，如果错误，提示是猜大了还是小了   

my_age = 30
user_input = int(input("input you guess num:"))
if user_input == my_age:
    print("congratulations, you get it !")
elif user_input > my_age:
    print("oh, think is bigger.")
else:
    print("think is smaller") 
    
    
    
    
