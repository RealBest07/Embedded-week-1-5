# print(list(range(-6,10,+3)))

# print("Embedded\
# System and\
#  Applications")

# print('''Embedded
# System''')

# a,b,c,d='embedded',539305,'System',3.142857
# print('%s %s is %s'%(a.title(),c,b))
# print('{0} {1} is {2}'.format(a.title(),c,b))
# print(f'{a.title()} {c} is {b}')

# a,b,c,d='embedded',539305,'System',3.142857
# print('The result of Pi or 22/7 is %.2f or %.4f'%(d,d))
# print('The result of Pi or 22/7 is {:.2f} or {:.4f}'.format(d,d))
# print(f'The result of Pi or 22/7 is {d:.2f} or {d:.4f}')

# m = input('Please enter somethings: ')
# print('Your input is '+m)

# n1 = int(input('Please enter first number: '))
# n2 = int(input('Please enter second number: '))

# re1 = n1+n2
# re2 = n1-n2
# re3 = n1*n2
# re4 = n1/n2

# print('Addition result is %s'%re1)
# print('Subtraction result is %s'%re2)
# print('Multiplication result %s'%re3)
# print('Division result is %.4f' %re4)

# num1=input("Please enter number ")
# print(num1.isnumeric())
# print(num1.isspace()) 

# num1 = input("Please Enter number(temp+): ")
# while not num1.isnumeric():
#     num1 = input('Alpha or special char are not allowed,try again: ')
# if num1.isnumeric() == True:
#     numi = int(num1)
#     if 5 <= numi <= 20:
#         print("your number is in range 5-20")
#     elif 5>numi or numi>20:
#         print("Invalid number")

# n = input('Please Enter number for create a Multiplication table: ')
# while not n.isnumeric():
#     n = input('invalid input, try again\n')
# n1 = int(n)
# i = 1
# re = 0
# print('Multiplication table of %s is here'%n1)
# for i in range(1,13):
#     re = i*n1
#     print('%s x %s = %s'%(n1,i,re))
#     i += 1
    
# 1+'a'
# t=[1,2,'s']
# t[3]
# 1/0
# print(z)
# g=[1,3]

# a=[-5,0,10,'m',20,3,0,5]
# for i in range(9):
#     try:
#         print(a[i]+5/a[i])
#     except ZeroDivisionError:
#         print('Found zero dividend')
#     except TypeError:
#         print('Wrong operand type')
#     except IndexError:
#         print('Out of index range')

# num1=input("Please enter number: ")
# try:
#     num1i=float(num1)
#     print("Your input Number is %.2f " %num1i)
# except ValueError:
#     print('Only numbers allowed!!')

t = input('''Please select
1 = toyota
2 = nissan
3 = benz
Your input: ''')
t = int(t)
a=0
while a == 0:
    if t not in [1,2,3]:
        t = input('Invalid brand, try again: ')
        t = int(t)
    elif t == 1:
        tot = input('There are 3 model available yaris, camry or revo: ')
        if tot not in ['yaris','camry','revo']:
            print('Invalid model, try again: ')
        else:
            print('Your car is toyota %s'%tot)
            a = 1
    elif t == 2:
        tot = input('There are 2 model available almera, march : ')
        if tot not in ['almera','march']:
            print('Invalid model, try again: ')
        else:
            print('Your car is nissan %s'%tot)
            a = 1
    elif t == 3:
        tot = input('There are 2 model available E300, GLC63 : ')
        if tot not in ['E300','GLC63']:
            print('Invalid model, try again: ')
        else:
            print('Your car is nissan %s'%tot)
            a = 1 