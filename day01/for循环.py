
#猜年龄游戏：实现让用户不断的猜年龄，但只给最多3次机会，再猜不对就退出程序。

my_age = 98
count = 0

while count <3:
   user_input = int(input("input you guess num:"))
   if user_input == my_age:
      print("congratuation,the num you guess is correctly!")
      break           #如果输入正确，就退出！
   elif user_input > my_age:
      print("the num you guess is bigger!")
   else:
       print("the num you guess is smaller!")
   count +=1
else:
    print("you are so garbage! the three times is wasted")


















