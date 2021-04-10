l=int(input("ENTER THE NUM"))
u=int(input("enter the num"))
flg=0
s=0
for i in range(l,u):
    if(u%i==0):
        flg=1
        break
    else:
        flg=0
        s=s+

if (flg==0):
    print("ITS A PRIME")
else:
    print("its not prime")

