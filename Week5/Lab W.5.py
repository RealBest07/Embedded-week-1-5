# import time as  t
# for i in  range(6):
#     print(t.ctime())
#     t.sleep(1)

# from datetime import timedelta
# a = timedelta(hours = 9,minutes=15,seconds=7)
# b = timedelta(hours = 16,minutes=20,seconds=28)
# dt = b-a
# print(dt)

# import csv
# import os
# import time as tt
# from datetime import datetime as dt
# try:
#     os.makedirs("c:\labweek05")
# except:
#     pass

# os.chdir('C:\labweek05\lab5')
# with open('lab524.csv','w+',newline='') as f:
#     mv=csv.writer(f)
#     mv.writerow(['Round','Hour','Minute','Second', 'microsecond'])
#     for i in range(10):
#         mv.writerow([i,dt.now().hour,dt.now().minute,dt.now().second,dt.now().microsecond])
#         tt.sleep(0.5)


# import os    #นำเช้า os
# import csv    #นำเช้า csv
# import numpy as np   #นำเช้า numpy

# os.chdir("c:\labweek05\lab5")   #เปลี่ยน Directory
# with open("lab525.csv","w",newline="") as f:   #สร้าง หรือ เปิด ไฟล์ lab525.csv ในโหมด w ย่อเก็บไว้ในตัวแปร f
#     mv = csv.writer(f)   #ใช้ csv.writer ในการเขียนไฟล์
#     mv.writerow(["radian","sin(x)","cos(x)","sin(5x)+cos(2x)"])   #เขียน Header ของตาราง
#     for i in np.linspace(0,2*np.pi,360):   #วนลูป i โดยการให้ i อยู่ในช่วง 0 ถึง 2*pi 360 จุด
#         mv.writerow([i,np.sin(i),np.cos(i),np.sin(5*i)+np.cos(2*i)])   #เขียนข้อมูลในแต่ row

# import os    
# import csv    
# import numpy as np
# import matplotlib.pyplot as plt
# os.chdir('C:\labweek05\lab5')
# k=np.genfromtxt('lab525.csv',delimiter=",",skip_header=1)
# x=k[:,0]
# y1=k[:,1]
# y2=k[:,2]
# y3=k[:,3]
# fig, axs = plt.subplots(2,2)
# axs[0,0].plot(x,y1,'b')
# axs[0,0].set_title('sin(x)')
# axs[0,1].plot(x,y2,'r')
# axs[0,1].set_title('cos(x)')
# axs[1,0].plot(x,y3,'g')
# axs[1,0].set_title('sin(5x)+cos(2x)')
# axs[1,1].plot(x,y1,'b')
# axs[1,1].plot(x,y2,'r')
# axs[1,1].plot(x,y3,'g')
# axs[1,1].set_title('All Signal')
# fig.tight_layout()
# plt.show()

import os    
import csv    
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import ptp
os.chdir('C:\labweek05\lab5')
x=[]
y1=[]
y2=[]
y3=[]
with open("lab525.csv","r",newline="") as f:
    csvw=csv.DictReader(f,delimiter=",")
    for row in csvw:
        x.append(row["radian"])
        y1.append(row["sin(x)"])
        y2.append(row["cos(x)"])
        y3.append(row["sin(5x)+cos(2x)"])
x=np.array(x,dtype=float)
y1=np.array(y1,dtype=float)
y2=np.array(y2,dtype=float)
y3=np.array(y3,dtype=float)
fig, axs = plt.subplots(2,2)
axs[0,0].plot(x,y1,'b')
axs[0,0].set_title('sin(x)')
axs[0,1].plot(x,y2,'r')
axs[0,1].set_title('cos(x)')
axs[1,0].plot(x,y3,'g')
axs[1,0].set_title('sin(5x)+cos(2x)')
axs[1,1].plot(x,y1,'b')
axs[1,1].plot(x,y2,'r')
axs[1,1].plot(x,y3,'g')
axs[1,1].set_title('All Signal')
fig.tight_layout()
plt.show()

# from datetime import datetime as dt
# from threading import Thread as th
# import time as tt
# def work1():
#     for i in range(10):
#         print('Thread1-%s %s.%s'%(i,dt.now().second,dt.now().microsecond))
#         tt.sleep(0.5)
# def work2():
#     for i in range(15):
#         print('Thread2-%s %s.%s'%(i,dt.now().second,dt.now().microsecond))
#         tt.sleep(0.2)

# myw1=th(target=work1)
# myw2=th(target=work2)

# myw1.start()
# myw2.start()

# from datetime import datetime as dt
# from threading import Thread as th
# import time as tt
# import os    
# import csv  
# import numpy as np
# os.chdir("c:\labweek05\lab5")   
# def work1():
#     with open("sine.csv","w",newline="") as f:  
#         mv = csv.writer(f) 
#         mv.writerow(['Round','Time(ms)','sine(x)'])
#         for i in range(30):
#             mv.writerow([i,dt.now().microsecond,np.sin(dt.now().microsecond)])
#             tt.sleep(0.1)
# def work2():
#     with open("cos.csv","w",newline="") as f:  
#         mv = csv.writer(f) 
#         mv.writerow(['Round','Time(ms)','cos(x)'])
#         for i in range(30):
#             mv.writerow([i,dt.now().microsecond,np.cos(dt.now().microsecond)])
#             tt.sleep(0.3)
# def work3():
#     with open("sqrtt.csv","w",newline="") as f:  
#         mv = csv.writer(f) 
#         mv.writerow(['Round','Time(ms)','sqrt(x)'])
#         for i in range(30):
#             mv.writerow([i,dt.now().microsecond,(dt.now().microsecond)**(1/2)])
#             tt.sleep(0.5)

# myw1=th(target=work1)
# myw2=th(target=work2)
# myw3=th(target=work3)

# myw1.start()
# myw2.start()
# myw3.start()