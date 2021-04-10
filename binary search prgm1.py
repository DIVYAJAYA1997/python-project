lst=[1,3,5,4]
n=int(input("ENTER THE sUM :"))
low=0
upp=len(lst)-1
for i in range(0,len(lst)):
    s=lst[low]+lst[upp]
    if(s==n):
        print(lst[low],lst[upp])
        low=low+1
    elif(s<n):
        low=low+1
    else:
        upp-=1




