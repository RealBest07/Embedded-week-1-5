# num1 = input('Please enter number: ')
# try:
#     num1i = float(num1)
#     print("Your input Number is %.2f "%num1i)
# except ValueError:
#     print("Only numbers allowed!!")
# else:
#     print("Thank you fot input")
# finally:
#     print('Program end')

# for i in [-5,0,10,'e',20,3,0,5]:
#     try:
#         if i == 'e':
#             raise Exception('Sorry Communication error')
#         print(i/1)
#     except Exception as err: #เก็บ Exception ใน err
#         print(err)

# def myfunc1():
#     print('Hello function1')
# myfunc1()

# def myfunc2(a,b):
#     c=a+b
#     print("the result is %s"%c)
# myfunc2(5,4)


# def pical():
#     mypi = 22/7
#     return mypi
# a = pical()
# print(a)

# def cirar(r):
#     ar = 3.14*r*r
#     return ar
# rrad = 5
# ca = cirar(rrad)
# print('Circle with radius = %s is %s'%(rrad,ca))

# def person(nam,money=100,car=2,pet=1):
#     print('Name: %s\nMoney: %s\nCar: %s\nPet: %s'%(nam,money,car,pet))
# person("man",100,1,2)
# person("girl",pet=5)

# fname=lambda x: x**2+2*x+1
# result1 = fname(1)
# print(result1)

# fname=lambda x,y: y*(x**2)+2*x*y+5
# result1 = fname(1,1)
# print(result1)

# fname=lambda x,y=1: y*(x**2)+2*x*y+5
# result1 = fname(1)
# print(result1)