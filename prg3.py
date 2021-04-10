text="abbac"
dict={}
for ch in text:
    if ch not in dict:
        dict[ch]=1
    else:
        dict[ch]+=1
for k,v in dict.items():
    if v==1:
        print(k,"is non recursive")
