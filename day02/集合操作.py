集合是一个无序的，不重复的数据组合，它的主要作用如下：
特点：
去重，把一个列表变成集合，就自动去重了
关系测试，测试两组数据之前的交集、差集、并集等关系

s = set([3,4,5,8,3,7,5])
t = set("hello3")
#print(s)        #output: {8, 3, 4, 5, 7}   自动去重

#集合的并集
a = t | s
print(a)        #output: {3, 4, 5, 'h', 7, 8, 'o', 'l', 'e'}   t 和 s 的并集

#集合的交集
b = s & t
print(b)       #output:   set()

#集合的差集
c = t - s
print(c)       #output:   {'h', '3', 'l', 'e', 'o'}  元素在t中，但是不在s中。

#集合的对称差集
d = t ^ s
print(d)        #output: {'h', 3, 4, 5, 'l', 7, 8, 'o', 'e', '3'} 元素在t或者s中，但是不在同时出现二者中。

##############集合添加元素###############
t.add('9')    #添加单项
print(t)      #output:    {'l', 'h', 'o', '9', '3', 'e'}

s.update([1,2])     #添加多项
print(s)      #output:   {1, 2, 3, 4, 5, 7, 8}

o = len(s)     #集合的长度
print(o)      #output:  7

################其他方法#########
x in s         #测试x是否是s的成员

x not in s         #测试x是否不是s的成员

s.issubset(t)
s <= t           #测试是否s中的每一个元素都在t中

s.issuperset(t)
s >= t            #测试是否t中的每一个元素都在s中

s.union(t)
s | t              #返回一个新的set包含s和t中的每一个元素

s.intersection(t)
s & t              #返回一个新的set包含s和t中的公共元素

s.difference(t)
s - t             #返回一个新的set包含s中有但是t中没有的元素

s.symmetric_difference(t)
s ^ t               #返回一个新的set包含s和t中不重复的元素

s.copy()          #返回set “s”的一个浅复制







