python range() 函数可创建一个整数列表，一般用在 for 循环中。

函数语法
range(start, stop[, step])

参数说明：
start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)


#示例：
#输出数字0到9
for r in range(10):
    print(r)         #output: 0 1 2 3 4 5 6 7 8 9

# #输入出3到9的数字
for r1 in range(3,10):
 print(r1)             #output:3 4 5 6 7 8 9

#输出0到9，步长为2
for r3 in range(0,10,2):
    print(r3)           #output: 0 2 4 6 8



#最简单的range循环
for i in range(10):
    print(i)
    
#############################################
#小于5的循环跳出，continue
for i in range(10):
    if i <5:
        continue
    print("loop:",i)
    
输出内容：
loop: 5
loop: 6
loop: 7
loop: 8
loop: 9 
    
#############################################
#大于5的循环跳出，break

for i in range(10):
    if i > 4:
        break
    print("loop:",i)
    
输出内容：
loop: 0
loop: 1
loop: 2
loop: 3
loop: 4
    
#############################################
#死循环
count = 0
while True:
    print("翠花，你是最棒的！",count)
    count +=1
输出内容：
翠花，你是最棒的！ 1
翠花，你是最棒的！ 2
翠花，你是最棒的！ 3
翠花，你是最棒的！ 4
........

###########################################
#循环固定次数
count = 0
while True:
    print("你是风儿我是傻子！",count)
    count +=1
    if count == 100:
        print("行了，就这儿吧。别送了。")
        break
 
输出内容：
.....
你是风儿我是傻子！ 97
你是风儿我是傻子！ 98
你是风儿我是傻子！ 99
行了，就这儿吧。别送了。

##################################################









