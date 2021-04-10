f=open("covid_19_india.csv","r")
dict={}
for lines in f:
    words=lines.rstrip("\n").split(",")
    state=words[3]
    cases=words[-1]
    if state not in dict:
        dict[state]=cases
    else:
        dict[state]=cases
print(dict)
for k,v in dict.items():
    data=sorted(dict,key=dict.get(" "),reverse=True)
print(data)







