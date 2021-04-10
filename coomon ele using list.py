lst=[1,3,4,5]
lst1=[3,4,5,6]
p=0
count=0
p2=0
for i in range(0,len(lst)):
    count+=1
    if lst[p]==lst1[p2]:
        print(lst[p])
        p+=1
        p2+=1
    elif lst[p]>lst1[p2]:
        p2+=1
    else:
        p+=1
print(count,"times")

