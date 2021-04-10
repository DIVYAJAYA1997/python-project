a={"ind":100,"china":200,"nz":10,"wi":40,"aus":35}
w=sorted(a,key=a.get)
print(w)
c=sorted(a,key=a.get,reverse=True)
print(c)