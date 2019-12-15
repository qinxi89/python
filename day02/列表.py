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

################################## 切 片 ################################
list = ['abao','xiaorang','kaier','huaan','jingke','zhuer']
#取下标1到4对应的列表元素，包括1，但是不包括4
s = list[1:4]
print(s)        #输出结果：['xiaorang', 'kaier', 'huaan']

#取下标1到列表倒数第二个元素的内容
s2 = list[1:-1]
print(s2)      #输出结果：['xiaorang', 'kaier', 'huaan', 'jingke']

#省略前下标，默认从0开始
s3 = list[:3]
print(s3)       #输出结果：['abao', 'xiaorang', 'kaier']

#省略后下标，默认取到最后一个
s4 = list[4:]
print(s4)       #输出结果：['jingke', 'zhuer']

#按步长取元素
s5 = list[0::2]       #从下标0开始取到最后一个位，每隔两个取
print(s5)             #输出结果：['abao', 'kaier', 'jingke']

#####################################追加###############################
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
