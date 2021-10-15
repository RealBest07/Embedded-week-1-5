from datetime import datetime as dt
today = [dt.now().day,dt.now().month,dt.now().year]
BD = [30,9,2021]
if BD == today:
    print('Happy Birthday!!')
    w = input('Message you want to tell me!!: ')
    print('Thanks you!!')
else:
    print('Not to day')

