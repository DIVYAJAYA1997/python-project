num=int(input("ENTER A NUMBER"))
anum=num
result=""
while(num!=0):
    r=num%10
    result+=str(r)
    num=num//10
print(result)
s=str(anum)
if(s==result):
    print("match")
else:
    print('mismatch')

