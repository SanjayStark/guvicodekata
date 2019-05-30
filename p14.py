a,b=input().split()
a=int(a)
b=int(b)
for i in range(a+1,b,2):
    if ((i//2)!=0):
        print(i)
