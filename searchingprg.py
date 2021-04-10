lst=[2,3,4,5,1,]
s=int(input("ENTER THE VALUE: "))
e=0
# for data in list:
#     flag=0
#     e=e+data
#     if(e==s):
#         flag=1
#         break
#     else:
flag=0
for i in range(0,len(lst)):
    e=e+lst[i]
    if(e==s):
        flag=1
    else:
        i=i+1
if(flag==1):
    print("HAVE A PAIR")
else:
    print("not a pair")








