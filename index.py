# i = input("请输入数字")
# t = input("请再输入数字")
# print(float(i) + float(t))

# scores = [60,70,80,90]
# print(scores[0:3])

# scores = (10,50,40,20)
# print(len(scores[0:3]))

# 函数
# def hello(name,age):
#     print("hello " + name + "今年" + str(age))
# hello("Ugg",18)

# def yearC(yearC1,yearC2):
#     print("一共：" + str(int(yearC1) + int(yearC2)))

# yearC(yearC1 = input("您工作几年了:"),yearC2 = input("您毕业几年了:"))

# if语句1
# working = False
# if working:
#     print("我在工作")
# else:
#     print("我没有在工作")

# if 语句2
# scorse = 32
# if scorse == 100:
#     print("100")
# elif scorse >= 80:
#     print(">= 80")
# elif scorse >= 60:
#     print(">= 60")
# else:
#     print("< 60")

# 练习 设计函数执行三个数比较找出最大
# def max_num(i,t,y):
#     print(max(i,t,y))
#     return 10
# print(max_num(20,30,80))

# for 语句
# for i in [0,1,2,3,4]:
#     print(i)

# for phrase in "hello 你好":
#     print(phrase)

# pow 函数
# import math
# print(math.pow(2,5))

# 读取二维数组
# numS = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [10]
# ]

# for numS1 in numS:
#     for num_def1 in numS1:
#         print(num_def1)

# 读取 写入 txt 文件
# 绝对路径 /Users/hugg/python/123.txt
# 相对路径 123.txt
# mode = "r" 读取
# mode = "w" 写入覆盖
# mode = "a" 写入追加

# file = open("123.txt" , mode="r")
# print(file.read())
# for line in file:
#     print(line.strip())
# file.close()

# with open("123.txt" , mode="a" , encoding="utf-8") as file:
#     file.write("\n你好")
# with open("123.txt" , mode="r" , encoding="utf-8") as file:
#     print(file.readlines())

# module 模组使用
# import max_num
# print(max_num.i,max_num.t)
# max_num.max_n(5,7,66)

# Create a sample collection
# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# # Strategy:  Iterate over a copy
# print(type(users))
# for user, status in users.copy().items():
#     if status == 'active':
#         del users[user]
# print(users)


# Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
# print(active_users)

# Emails = {'google':'@gmail.com', 'msn':'@msn.com', '126':'@126.com'}

# d = max(map(len, Emails.keys()))    #获取key的最大值
# print(d)
# for key,values in Emails.items():
#      print(key.rjust(d),":",values)

# mac测试