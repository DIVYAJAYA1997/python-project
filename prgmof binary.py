lst=[]
n=int(input("ENTER THE SIZE OF LIST:  "))
for i in range (0,n):
    e=int(input("ENTER THE LIST ELEMENT : "))
    lst.append(e)
print(lst)
a=int(input("ENTER THE NUM :"))
s=0
flag=0
for i in range(0,n):
    for j in range(0,n):
        s=s+lst[j]
        if(s!=a):
            j=j+1
        else:
            flag=0
            break
if(flag==0):
    print("PAIR EXIST")
else:
    print("PAIR DOESNOT EXIST")




