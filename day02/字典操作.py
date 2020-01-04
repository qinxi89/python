字典一种key - value 的数据类型，使用就像我们上学用的字典，通过笔划、字母来查对应页的详细内容。
字典的特性：
dict是无序的
key必须是唯一的,天生去重

dict = {
    'stu01' : "miya",
    'stu02' : "cuihua",
    'stu03' : "fengrun",
}

######################################## 增 加 #########################################
dict['stu05'] = 'qinxi'
print(dict)        #输出内容：{'stu02': 'cuihua', 'stu03': 'fengrun', 'stu01': 'miya', 'stu05': 'qinxi'}



######################################## 修 改 #########################################
#修改
dict['stu03'] = "zhengzhou"
print(dict)      #输出内容：{'stu01': 'miya', 'stu05': 'qinxi', 'stu03': 'zhengzhou', 'stu02': 'cuihua'}


######################################## 删 除 #########################################
#指定元素删除
dict.pop('stu01')
print(dict)      #输出内容：{'stu05': 'qinxi', 'stu02': 'cuihua', 'stu03': 'zhengzhou'}

del dict['stu03']
print(dict)        #输出内容：{'stu05': 'qinxi', 'stu02': 'cuihua'}
#随机删除
dict.popitem()
print(dict)       #随机输出内容：{'stu02': 'cuihua'}



######################################## 查 找 #########################################
d1 = 'stu01' in dict
print(d1)          # 返回内容：True

#获取key对应的内容
d2 = dict.get('stu01')
print(d2)        #返回内容： miya

d3 = dict['stu03']
print(d3)        #返回内容： fengrun



######################################## 多级字典嵌套 #########################################
av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}

a = av_catalog['大陆']['1024']
print(a)             #output:  ['全部免费,真好,好人一生平安', '服务器在国外,慢']
b = av_catalog['欧美']['letmedothistoyou.com']
print(b)             #output:  ['多是自拍,高质量图片很多', '资源不多,更新慢']


######################################## 字典循环 #########################################
#打印字典中key和值
dict = {
    'stu01' : "miya",
    'stu02' : "cuihua",
    'stu03' : "fengrun",
}
#1,
for key in dict:
    print(key, dict[key])           
#output: stu01 miya
stu03 fengrun
stu02 cuihua


#2,
for k, v in dict.items():          ##会先把dict转成list,数据里大时莫用
    print(k,v)
#output: stu01 miya
stu03 fengrun
stu02 cuihua


##################################### 字典的 其他方法 #####################################
Python 字典 fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。


seq = ('Google', 'Runoob', 'Taobao')
dict = dict.fromkeys(seq)
print("新字典为： %s " % str(dict)) #output: 新字典为： {'Taobao': None, 'Runoob': None, 'Google': None}

dict = dict.fromkeys(seq, 10)
print("新字典为： %s" % str(dict))   #output: 新字典为： {'Taobao': 10, 'Runoob': 10, 'Google': 10}

dict2 = {}
dict2 = dict2.fromkeys(range(4),'赞')
print(dict2)                     #output: {0: '赞', 1: '赞', 2: '赞', 3: '赞'}













