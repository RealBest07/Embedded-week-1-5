# from datetime import date

# t=date.today()
# print(t.year)


# from datetime import datetime

# # n=datetime(2017,11,22,23,55,59,30000)
# n=datetime.now()
# print(n.strftime('%B %A %d %Y, %x %X'))

# from datetime import *
# # from datetime import datetime
# # import datetime
# import time
# a=datetime.now()
# time.sleep(2.5)
# b=datetime.now()

# c=timedelta(days=a.day,hours=a.hour,minutes=a.minute,seconds=a.second,microseconds=a.microsecond)
# d=timedelta(days=b.day,hours=b.hour,minutes=b.minute,seconds=b.second,microseconds=b.microsecond)
# e=d-c
# print(e)

# import os
# print('my dir =',os.getcwd())

# os.mkdir('hello')
# import os 
# # os.makedirs("d:/w555")
# f = open("d:/w555/newfile.txt","a+")
# # f.write('\nembedded')
# f.seek(0)
# s=f.read()
# f.close()
# print(s)