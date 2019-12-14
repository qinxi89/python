#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2019/12/14 7:19 下午
# @Author  : qinxi
# @Site    : www.iqinxi.com
# @File    : test.py
#2019


#list 列表
member = [1,2,3,4,5]
print(member)           #输出 结果：[1, 2, 3, 4, 5]

#append（）方法
member.append('qinxi')
print(member)           #输出结果： [1, 2, 3, 4, 5, 'qinxi']

#member.append('you','黑夜')
#print(member)           # 输出结果： TypeError: append() takes exactly one argument (2 given)，
#append() 方法只能追加一个元素。

#extend()方法
member.extend(['test','加油'])
print(member)          #输出结果：[1, 2, 3, 4, 5, 'qinxi', 'test', '加油']

#len() 方法

s = len(member)
print(s)        #输出结果 ：8  ；具体元素为：[1, 2, 3, 4, 5, 'qinxi', 'test', '加油']

# insert（）方法，在数组中下标后插入
member.insert(2,'miya')
print(member)     #输出结果：[1, 2, 'miya', 3, 4, 5, 'qinxi', 'test', '加油']


#删除数组中的元素
del member[3]     #删除元素下标为3的元素
del member        #删除整个member数组
print(member)

