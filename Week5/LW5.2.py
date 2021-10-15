import os
try:
    os.makedirs("d:\w5x")
except:
    print("folder exist!!")

# os.chdir("d:\w5x")
# f = open("hello.txt","r")
# s=f.read()
# print(s)
# f.close()


# os.chdir("d:\w5x")
# f = open("hello.txt","r+")
# s=f.write("222")
# # print(s)
# f.close()

# os.chdir("d:\w5x")
# f = open("hello.txt","w")
# f.write('Hello world')
# f.close()

os.chdir("d:\w5x")
# with open("hello.txt","a") as f:
#     f.write('\nHello world')
from datetime import datetime as dt
import csv
import time as tt
# with open("book2.csv",'w',newline="")as f:
#     csvw=csv.writer(f)
#     csvw.writerow(["date","temp","volt"])
#     for i in range(20):
#         # tt.sleep(1)
#         csvw.writerow([i,i**2,2.5*i])


# with open("book2.csv",'w',newline="")as f:
#     csvw=csv.writer(f,delimiter='/')
#     csvw.writerow(["date","temp","volt"])
#     for i in range(20):
#         # tt.sleep(1)
#         csvw.writerow([i,i**2,2.5*i])


# with open("book2.csv",'r',newline="")as f:
#     csvw=csv.reader(f)
#     dtl=list(csvw)
#     print(dtl)

# เรียกplot จาก csv
import numpy as np
import matplotlib.pyplot as plt
x=[]
y1=[]
y2=[]
with open("book2.csv",'r',newline="")as f:
    csvw=csv.DictReader(f,delimiter=",")
    for row in csvw:
        x.append(row["date"])
        y1.append(row["temp"])
        y2.append(row["volt"])
print(x)
x=np.array(x,dtype=float)
y1=np.array(y1,dtype=float)
y2=np.array(y2,dtype=float)

plt.plot(x,y1)
plt.plot(x,y2)
plt.show()

# k=np.genfromtxt('book2.csv',delimiter=",",skip_header=1)
# # print(k)
# x=k[:,0]
# y1=k[:,1]
# y2=k[:,2]
# plt.plot(x,y1)
# plt.plot(x,y2)
# plt.show()