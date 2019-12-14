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


#pop列表分片,分片仅仅是取出这“片”的数据，并不会改变列表本身。
 member.pop()         #括号里没有参数，表示删除list数组中最后一个元素
 print(member)

#pop(index)，用作于删除制定下标的元素，并且返回删除后的元素列表
member.pop(2)
print(member)


list = ['123','翠花','456']
p = '123' in list
print(p)         #返回结果：True

t = list.index('翠花')
print(t)         #返回结果：1

#列表前后元素翻转，reverse()
list.reverse()
print(list)           #输出结果：['456', '翠花', '123']

#列表元素排序，默认从小到大排序，sort()              *****
list1 = [1,3,17,2,7,20,4,6,10]
list1.sort()
print(list1)           #输出结果： [1, 2, 3, 4, 6, 7, 10, 17, 20]

#列表元素排序 sort,从大到小排序
list1.sort(reverse=True)
print(list1)
