from datetime import datetime as dt
import time as tt
from threading import Thread as th
import numpy as np
import matplotlib.pyplot as plt
# def w1():
#     for i in range(10):
#         print("w1 s.us=%s.%s i=%s"%(dt.now().second,dt.now().microsecond,i))
#         # tt.sleep(0.5)
# def w2():
#     for i in range(10):
#         print("w2 s.us=%s.%s i=%s"%(dt.now().second,dt.now().microsecond,i))
#         # tt.sleep(0.75)

# myw1=th(target=w1)
# myw2=th(target=w2)

# myw1.start()
# myw2.start()

# w1()
# w2()
##############################################################################################
class mw(th):
    def __init__(self,wn,dly):
        th.__init__(self)
        self.wn=wn
        self.dly=dly
    def run(self) -> None:
        for i in  np.arange(10):
            print("%s s.us=%s.%s i=%s"%(self.wn,dt.now().second,dt.now().microsecond,i))
            tt.sleep(self.dly)

myw1=mw("w1",0.5)
myw2=mw("w2",0.75)
myw1.start()
myw2.start()