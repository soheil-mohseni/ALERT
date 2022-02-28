#! /usr/bin/python


import datetime as dt
from datetime import timedelta

def time():
    now = dt.datetime.now()
    print(now)
    start = input('when do you exactly take a medcine?Enter your Date:(e.g. 2022/02/18 21:20:30)')
    end = dt.datetime.strptime(start, "%Y/%m/%d %H:%M:%S")
    kip = input('What is the time interval between taking the same medicine?')
    use = dt.datetime.strptime(kip, "%H")
    print(type(end.date))
    print(type(use))
    print(type(end))
    print(type(end.hour))
    print(type(use.hour))
    equal = ((end + timedelta(hours=use.hour)))
    #print (equal)
    #equals = dt.datetime.strptime(equal, "%Y/%m/%d %H:%M:%S")
    mines = ((equal - timedelta(minutes=30)))
    #print(mines)
    
    if now.hour == mines.hour :
        if now.minute == mines.minute :
            print("hey body 30 minutes later you should take your medcine")
            
    if now.hour == equal.hour :
        if now.minute == equal.minute :
            print("hey body you should take your medcine")
            
        
    
    
time()
