class cicle:
    def __init__(self,rad) -> None:
        self.rad=rad
        self.ar=0
        self.cir=0
        self.area()#เป็นการรันโดยอัตโนมัติ
        self.circum()#เป็นการรันโดยอัตโนมัติ
    def area(self):
        self.ar = 3.14*(self.rad**2)
    def circum(self):
        self.cir = 2*3.14*self.rad

class rect:
    def __init__(self,s1,s2) -> None:
        self.s1=s1
        self.s2=s2
        self.rec_ar=0
        self.rec_l=0
        self.area()#เป็นการรันโดยอัตโนมัติ
        self.reclng()#เป็นการรันโดยอัตโนมัติ
    def area(self):
        self.rec_ar = self.s1*self.s2
    def reclng(self):
        self.rec_l = (self.s1*2)+(self.s2*2)

def pical():
    pival = 22/7
    return pival

k = 25.3