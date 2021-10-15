# for i in range(1,11):
#     k=i%5
#     if k==0:
#         raise Exception("Found zero residual!")
#     else:
#         print(i)

# for i in range(1,11):
#     try:
#         k=i%5
#         if k==0:
#             raise Exception("Found zero residual!")
#         else:
#             print(i,end=" ")
#     except Exception as err:
#         print(err,end=(''))
#     else:
#         print("Residual = %s"%k,end=(''))
#     finally:
#         print(" Done")

# for i in [-5,'a',10,'e',20,3,'b',5]:
#     try:
#         if i == 'a' or i == 'b':
#             raise Exception("Communication error")
#         else:
#             print(i)
#     except Exception as err:
#         print(err)
#     else:
#         pass
#     finally:
#         pass

# def myDtel(name,Sname,age):
#     print('''Name: %s
# Surname: %s
# Age: %s
# I Love Embedded''' %(name,Sname,age))

# myDtel('Somsak','Srithai',25)

# import math

# def quadSol(a,b,c):
#     dis = b * b - 4 * a * c 
#     sqrt_val = math.sqrt(abs(dis)) 
#     sol1 = ((-b + sqrt_val)/(2 * a))
#     sol2 = ((-b - sqrt_val)/(2 * a))

#     return(sol1,sol2)

# x1,x2 = quadSol(5,2,7)
# print ('x1 = %s\nx2 = %s' % (x1,x2))

# def quadSol(a,b,c):
#     sol1 = (-b+(b**2-4*a*c)**(0.5))/(2*a)
#     sol2 = (-b-(b**2-4*a*c)**(0.5))/(2*a)

#     return(sol1,sol2)

# # a,b,c = 5,2,7
# # x1,x2 = quadSol(a,b,c)
# # print("The x value from equation %sx\u00b2 + %sb + %s = 0 "%(a,b,c))
# # print ('x1 = %s\nx2 = %s' % (x1,x2))
# # print(type(x1))
# # print(type(x2))

# a,b,c = 5,2,7
# x = quadSol(5,2,7)
# print("The x value from equation %sx\u00b2 + %sb + %s = 0 "%(a,b,c))
# print ('x1 = %s\nx2 = %s' % (x[0],x[1]))
# print(type(x[0]))
# print(type(x[1]))
# print(type(x))

# xplus = lambda a,b,c : ((-b+(b**2-4*a*c)**(0.5))/(2*a))
# xminus = lambda a,b,c : ((-b-(b**2-4*a*c)**(0.5))/(2*a))
# x1 = xplus(5,2,7)
# x2 = xminus(5,2,7)
# print ('x1 = %s\nx2 = %s' % (x1,x2))

# class embedded:
#     x=5
#     y=3

# test = embedded()
# print(test.x)
# print(test.y)

# embedded.z=120
# print(test.z)

# class database:
#     def __init__(self,name,pet,car):
#         self.name=name
#         self.pet=pet
#         self.car=car
#         print('This is constructor')
#     def mymethod(self):
#         print('This is method')
# person1 = database("Lisa","cat","Tesla")
# person2 = database('Ryan','dog', 'BMW')
# person1.pet = 'rabbit'
# print(vars(person1))
# database.Country = 'USA'
# print(vars(database))

# class quadSol:
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#     def xplus(self,a,b,c):
#         self.x1=((-b+(b**2-4*a*c)**(0.5))/(2*a))
#     def xminus(self,a,b,c):
#         self.x2=((-b-(b**2-4*a*c)**(0.5))/(2*a))

# eq = quadSol(5,2,7)  	
# eq.xplus(5,2,7)    			
# eq.xminus(5,2,7)		
# print("The x value from equation %sx\u00b2 + %sb + %s = 0 "%(eq.a,eq.b,eq.c))	
# print('x1= %s\nx2= %s' % (eq.x1,eq.x2))	

# class quadSol:
#     def __init__(self):
#         self.a=0
#         self.b=0
#         self.c=0
#     def xplus(self):
#         self.x1=((-self.b+(self.b**2-4*self.a*self.c)**(0.5))/(2*self.a))
#     def xminus(self):
#         self.x2=((-self.b-(self.b**2-4*self.a*self.c)**(0.5))/(2*self.a))

# eq = quadSol()	
# eq.a = 5
# eq.b = 2
# eq.c = 7
# eq.xplus()    			
# eq.xminus()		
# print("The x value from equation %sx\u00b2 + %sb + %s = 0 "%(eq.a,eq.b,eq.c))		
# print('x1= %s\nx2= %s' % (eq.x1,eq.x2))	


