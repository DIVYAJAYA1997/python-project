t="abbc"
dict={}
for ele in t:
    if ele not in dict:
        dict[ele]=1
    else:
        print(ele,"is recursive char")
        break



