import re
rule="[K][L]\d{2}[A-Z]{2}\d{4}"
lis=[]
f=open("text","r")
for words in f:
    word=words.rstrip("\n")
    match=re.fullmatch(rule,word)
    if match!=None:
        lis.append(word)
print(lis)





