#/D
import re
p='\D'
ma=re.finditer(p,"abc _Z7K@")
for ele in ma:
    print(ele.start())
    print(ele.group())
#/d
P='/d'
mac=re.finditer(P,"abc _Z7K@")
for ele in mac:
    print(ele.start())
    print(ele.group())
#/w
A='/W'
Match=re.finditer(A,"abc _Z7K@")
for ele in Match:
    print(ele.start())
    print(ele.group())
a='/w'
m=re.finditer(a,"abc _Z7K@")
for ele in m:
    print(ele.start())
    print(ele.group())

