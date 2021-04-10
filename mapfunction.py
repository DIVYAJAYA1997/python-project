lst=[1,2,3,4,5]
sq=list(map(lambda n:n**2,lst))
print(sq)
lis=["asdf","erty","zxcvb"]
upp=list(map(lambda l:l.upper(),lis))
print(upp)
a=[1,4,6,7,3]
fun=list(map(lambda num:num+1 if num>5 else num-1,a))
print(fun)


