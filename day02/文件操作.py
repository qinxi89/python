
对文件操作流程
1、打开文件，得到文件句柄并赋值给一个变量
2、通过句柄对文件进行操作
3、关闭文件 

f = open('./1.txt')        #打开文件
first_line = f.readline()
print('first_line:',first_line)      #读一行
print('我是分割线'.center(50,'-'))
data = f.read()      #读取剩下文件的所有内容，文件大时，不要用
print(data)        #打印文件

f.close()          #关闭文件

打开文件的模式有：

r，只读模式（默认）。
w，只写模式。【不可读；不存在则创建；存在则删除内容；】
a，追加模式。【可读；   不存在则创建；存在则只追加内容；】
"+" 表示可以同时读写某个文件

r+，可读写文件。【可读；可写；可追加】
w+，写读
a+，同a

"U"表示在读取时，可以将 \r \n \r\n自动转换成 \n （与 r 或 r+ 模式同使用）

rU
r+U

"b"表示处理二进制文件（如：FTP发送上传ISO镜像文件，linux可忽略，windows处理二进制文件时需标注）

rb
wb
ab


############################################# with语句 ##########################################

为了避免打开文件后忘记关闭，可以通过管理上下文，即：
with open('log','r') as f:
     
    ...
如此方式，当with代码块执行完毕时，内部会自动关闭并释放文件资源。

在Python 2.7 后，with又支持同时对多个文件的上下文进行管理，即：
with open('log1') as obj1, open('log2') as obj2:
    pass

#############################################  input 函数  ######################################

input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回。
例子：
while True:
  str = input("请输入：")
  print("你输入的内容是：",str)

############################################ 打开和关闭文件 #######################################
open函数，用Python内置的open()函数打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写。
file object = open(file_name [, access_mode][, buffering])

File对象的属性
一个文件被打开后，你有一个file对象，你可以得到有关该文件的各种信息
file.closed 	返回true如果文件已被关闭，否则返回false。
file.mode	    返回被打开文件的访问模式。
file.name	    返回文件的名称。
file.softspace	如果用print输出后，必须跟一个空格符，则返回false。否则返回true。


fo = open("foo.txt", "w")
print("文件名：", fo.name)            #output:foo.txt
print("是否已经关闭", fo.closed)       #output: False
print("访问模式：", fo.mode)           #output: w
print("末尾是否强制加空格：", fo.softspace)   #python 3中不再支持

########################################## write()方法 #######################################
write()方法可将任何字符串写入一个打开的文件。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。
write()方法不会在字符串的结尾添加换行符('\n')：
语法：
fileObject.write(string)

例子：
fo = open("foo.txt", "w")
fo.write("www.baidu.com,\nvery good site!\n")
fo.close()

######################################### read()方法 #######################################
read（）方法从一个打开的文件中读取一个字符串。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。
语法：
fileObject.read([count])
在这里，被传递的参数是要从已打开文件中读取的字节计数。该方法从文件的开头开始读入，如果没有传入count，它会尝试尽可能多地读取更多的内容，很可能是直到文件的末尾。
例子：
fo1 = open("foo.txt", "r+")
str = fo1.read()
print("读取的字符是：\n", str)
fo1.close()


########################################### close 函数 ########################################
File 对象的 close（）方法刷新缓冲区里任何还没写入的信息，并关闭该文件，这之后便不能再进行写入。
当一个文件对象的引用被重新指定给另一个文件时，Python 会关闭之前的文件。用 close（）方法关闭文件是一个很好的习惯。

例子：
fo = open("foo.txt", "w")
print("文件名：", fo.name)     #output:文件名： foo.txt
fo.close()
print("文件是否关闭：", fo.closed)        #output: True

######################################### 文件定位 ###########################################
tell()方法告诉你文件内的当前位置, 换句话说，下一次的读写会发生在文件开头这么多字节之后。

seek（offset [,from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。
如果from被设为0，这意味着将文件的开头作为移动字节的参考位置。如果设为1，则使用当前的位置作为参考位置。如果它被设为2，那么该文件的末尾将作为参考位置。


例子：
#read()方法
fo = open("foo.txt", "r+")
str = fo.read()
print("读取的字符是：",str)    #output: www.baidu.com,very good site!

#查找当前位置
position = fo.tell()
print("文件当前位置：",position)  #output:31

#把指针重新定位到文件开头
position = fo.seek(0,0)
str = fo.read(10)
print("重新读取字符串：",str)   #output:  www.baidu.
fo.close()

########################################## rename()方法  #######################################
#rename()方法需要两个参数，当前的文件名和新文件名。
语法：
os.rename(current_file_name, new_file_name)

#例子
# os.rename("foo.txt","qinxi.txt")

########################################## remove()方法 ######################################
#remove()方法，你可以用remove()方法删除文件，需要提供要删除的文件名作为参数。
语法：
os.remove(file_name)
例子：
#os.remove("qinxi.txt")

######################################### mkdir()方法 ########################################
#mkdir()方法，可以使用os模块的mkdir()方法在当前目录下创建新的目录们。你需要提供一个包含了要创建的目录名称的参数。
语法：
os.mkdir("newdir")

######################################## chdir()方法 ########################################
# #chdir()方法，可以用chdir()方法来改变当前的目录。chdir()方法需要的一个参数是你想设成当前目录的目录名称。
语法：
os.chdir("newdir")
例子：
os.chdir("cuihua")
fo = open("foo.txt", "w")
fo.write("this is a test file..")

####################################### getcwd()方法 #####################################
#getcwd()方法显示当前的工作目录。
语法：
os.getcwd()
#例子
print("当前工作目录：", os.getcwd())     #output: 当前工作目录： /Users/芹溪/python/test/cuihua

###################################### rmdir()方法 #######################################
#rmdir()方法
mdir()方法删除目录，目录名称以参数传递。在删除这个目录之前，它的所有内容应该先被清除。

语法：
os.rmdir('dirname')
#例子
os.chdir("/Users/芹溪/python/test/cuihua")
os.remove("foo.txt")
os.chdir("/Users/芹溪/python/test")
os.rmdir("cuihua")





















