a=[2,6,5,9,3]
e=int(input("ENTER THE NUM U WANT TO SEARCH:  "))
flag=0
for data in a:
    if(data==e):
        flag=1
        break
    else:
        flag=0
if(flag==1):
    print("ELEMENT FOUND")
else:
    print("ELEMENT NOT FOUND")


