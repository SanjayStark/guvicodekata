y=int(input())
if ((y%4==0) or (y%400==0) and (y%400!=0)):
    print("Leap year")
else:
    print("Not Leap year")
