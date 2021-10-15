# num1 = input("Enter your number: ")
# print('Your number is : ' + num1)
# num1 = int(num1)
# print(type(num1))
# print(num1.isnumeric())

# Ex01
# num1 = input("Please Enter number 1-10: ")
# numi = int(num1)
# if 1 <= numi <= 10:
#     print("your number is in range 1-10")
# else:
#     print("Invalid number")

# Ex02
# num1 = input("Pleae enter number 1-10: ")
# numi = int(num1)
# if 1 <= numi <= 10:
#     print("your number is in range 1-10")
# elif 11 <= numi <= 50:
#     print("your number is in range 11-50")
# elif numi > 50:
#     print("Over limitation")
# elif numi < 0:
#     print("Must be possitive")

# for
# for i in [1,2,5,6,8,"apple","mg"]: 
#     print(i)

# for i in range(1,10):
#     print(i)

# i=4
# if i in [1,3,5,6]:
#     print('i is a member')
# else:
#     print('i is not a member')

# Ex03
# num1 = input("Please enter number: ")
# num1 = int(num1)
# r = 1
# for i in range(1,num1+1):
#     r = i*r
# print("factorial of %s is %s" %(num1,r))

# while
# x = 1
# while(x<5):
#     print(x)
#     x += 1

# Ex04
# num1 = input("Pleae enter number 1-5: ")
# num1 = int(num1)
# while num1<1 or num1>5:
#     num1 = input("Invalid try again: ")
#     num1 = int(num1)
# print('Your input number is %s'%num1)

# for i in range(-2,3):
#     try:
#         print(6/i)
#     except :
#         print("Something went wrong")

# for i in range(-2,3):
#     try:
#         print(h)
#     except ZeroDivisionError:
#         print("Something went wrong")
#     except NameError:
#         print('Name Error')

# 5/'m'