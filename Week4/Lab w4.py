# import numpy as np
# h = np.ones((6,6),dtype=int)
# print(h)

# h = np.arange(2,10)
# print(h)

# h = np.arange(1,13).reshape(6,2)
# print(h)

# k = np.arange(6); print(k)

# b = np.arange(24).reshape(6,2,2)
# print(b.shape)

# apple=np.array([30,20,50,70,25,35,55])
# grape=np.array([20,85,33,47,21,95,71])
# durian=np.array([85,120,78,88,54,32,27])
# orange=np.array([44,21,65,33,25,25,77])
# kivi=np.array([77,22,58,79,82,55,64])

# fruit=np.array([apple,grape,durian,orange,kivi])
# print(fruit)

# print(fruit.sum(axis=0))#sum colum
# print(fruit.sum(axis=1))#sum row


# a=np.array([[1,1,1],[2,-1,2],[1,1,-2]])
# c=np.array([2,-5,-1])

# # b=np.invert(a)*c
# b = np.linalg.solve(a,c)
# print(b)

# import matplotlib.pyplot as plt
# x = np.arange(0,20,0.1)
# y1 = np.sin(x)
# y2 = np.cos(x/3)
# y3 = np.cos(2*x)+np.sin(x)
# plt.figure(1,figsize=[4,6],dpi=60)
# plt.plot(x,y1,'r--')
# plt.plot(x,y2,'k-.')
# plt.plot(x,y3,'m .')

# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# x = np.arange(0,20,0.1)
# y1 = np.sin(x)
# y2 = np.cos(x/3)
# y3 = np.cos(2*x)+np.sin(x)

# fig=plt.figure(1)
# ax=fig.gca()
# ax.set_title('sine wave and cos wave')
# ax.set_xlabel('Time(s)')
# ax.set_ylabel('Amplitude(arb)')
# ax.plot(x,y1,'b:',label='sin(t)',ms=0.5)
# ax.plot(x,y2,c=(1,0.8,0.3),ls='--',label='sin(t/3)',ms=0.5)
# ax.plot(x,y3,c=(0.4,0.7,0.3),ls='-.',label='cos(2*t)+sin(t)',ms=0.5)
# ax.set_xlim([0,11])
# ax.legend(loc=0)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# x = np.arange(0,12,0.1)
# y1 = np.sin(x)
# y2 = (np.sin(x))**2
# y3 = np.cos(x**2)
# y4 = 8*np.sin(5*x)+(x**2)

# fig,axs = plt.subplots(1,3)
# axs[0].plot(x,y1,'b')
# axs[0].set_title('sin(x), $sine^{2}(x)$')
# axs[0].plot(x,y2,'r')
# axs[1].plot(x,y4,c=(0.4,0.7,0))
# axs[1].set_title('8sin(5x)+$x^{2}$')
# axs[2].plot(x,y3,'m')
# axs[2].set_title('cos($x^{2}$)')

# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# x = np.arange(0,12,0.1)
# y1 = np.cos(x**2)
# y2 = 8*np.sin(5*x)+(x**2)

# fig=plt.figure(2)
# ax=fig.gca()
# ax.set_title('8sin(5x)+$x^{2}$ and cos($x^{2}$)')
# ax.plot(x,y2,label='cos($x^{2}$)')
# ax2=ax.twinx()
# ax2.plot(x,y1,'m',label='8sin(5x)+$x^{2}$')
# ax.legend(loc=2)
# ax2.legend(loc=6)
# plt.show()

from lab4module import cirarea, quadsol
my_area=cirarea(1)
print(my_area)
k=quadsol(2,3,5)
print("the solution of equation %sx\u00b2+%sx+%s \
is\nX1= %s\nX2=%s"%(k.a,k.b,k.c,k.x1,k.x2))
k.ploteq()