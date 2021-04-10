f=open("demo","r")
dict={}
stopwords=["the","is","and","were","was","where","how","an","at","a","than","who"]
for lines in f:
    w=lines.rstrip("\n").split(" ")
    for word in w:
        if word in stopwords:
            pass
        else:
            if word not in dict:
                dict[word]=1
            else:
                dict[word]+=1
print(word)






