t="hello hai how hello hai"
w=t.split(" ")
print(w)
dict={}
for ele in w:
    if ele not in dict:
        dict[ele]=1
    else:
        dict[ele]+=1
        break
print(dict)
data=sorted(dict,key=dict.get)
print(data)
data=sorted(dict,key=dict.get,reverse=True)
print(data[0])










