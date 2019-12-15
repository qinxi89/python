#Python 的元组与列表类似，不同之处在于元组的元素不能修改。
#元组使用小括号，列表使用方括号。
#元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2019/12/14 9:27 下午
# @Author  : qinxi
# @Site    : www.iqinxi.com
# @File    : test1.py

#定义一个元组，括号不是必须的，逗号才是元组的关键。
tuple = (1,2,3,4,5,8,10)
tuple1 = 9,10,20,64
print(tuple)       #输出内容：(1, 2, 3, 4, 5, 8, 10)
print(tuple1)      #输出内容：(9, 10, 20, 64)

#取下标元组
tuple2 = tuple[:3]
print(tuple2)

#元组元素不可更改
tuple[1] = 11
print(tuple2)     #输出内容：TypeError: 'tuple' object does not support item assignment


#创建空列表，空元组
temp1 = []
temp = ()
print(temp)       #输出内容：（）
print(temp1)      #输出内容：[]

s = type(temp)
print(s)            #输出内容：<class 'tuple'>

#更新元组，原理：切片添加，把原来的元组拆分两部分，将新的元素加进去，构成新的元组，贴上新的标签覆盖原标签，原来的元组仍然存在，只是没有标签指向等待Python回收器将原来的元组扔掉
temp = ('阿莫','韦德','罗纳尔多','刘邦')
temp = temp[:2] + ('哈尔',) + temp[2:]
print(temp)

#删除元组,可以利用和添加元组元素同样的原理，切片删除
#删除整个元组
del temp     #如果没有显式的调用del方法删除，Python回收机制也会定期检查，当发现元组没有标签指向的时候，也会释放元组资源
#也会释放元组资源
print(temp)



