import numpy as np
import matplotlib.pyplot as plt

class quadsol:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        self.x1=0
        self.x2=0
        self.x=0
        self.xplus()
        self.xminus()
    def xplus(self):
        self.x1=((-self.b+(self.b**2-4*self.a*self.c)**(0.5))/(2*self.a))
    def xminus(self):
        self.x2=((-self.b-(self.b**2-4*self.a*self.c)**(0.5))/(2*self.a))
    def ploteq(self):
        self.x = np.arange(-100,100)
        self.y = self.a*(self.x**2)+self.b*self.x+self.c
        plt.plot(self.x,self.y)
        plt.show()

def cirarea(r):
    ar=3.141*r**2
    return  ar
