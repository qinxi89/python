#汉诺塔游戏

def hanoi(n, x, y, z):
    if n == 1:
        print(x, '>>>>', z)
    else:
        hanoi(n-1, x, z, y)
        print(x, '>>>>', z)
        hanoi(n-1, y, x, z)
n = int(input("请输入汉罗塔的层数："))
hanoi(n,'X', 'Y', 'Z')
