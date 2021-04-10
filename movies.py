f=open("movies.csv","r")
dict={}
y=[]
for lines in f:
    words=lines.rstrip("\n").split(",")
    movie=words[1]
    year=words[2]
    if movie not in dict:
        dict[movie]=year
for k,v in dict.items():
    y.append(dict[v])
    lat=max(y)
    if v==lat :
        print(dict[movie],"is the latest movie relesed")
    else:
        break









