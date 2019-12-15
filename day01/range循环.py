

#最简单的range循环
for i in range(10):
    print(i)

#小于5的循环跳出，continue
for i in range(10):
    if i <5:
        continue
    print("loop:",i)

#大于5的循环跳出，break

for i in range(10):
    if i > 4:
        break
    print("loop:",i)
