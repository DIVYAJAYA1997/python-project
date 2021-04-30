iplpoints=[
    {"team":"csk","mp":6,"won":5,"los":1,"pts":10},
    {"team":"srh","mp":6,"won":1,"los":5,"pts":2},
    {"team":"rcb","mp":6,"won":5,"los":1,"pts":10},
    {"team":"csk","mp":6,"won":5,"los":1,"pts":10},
    {"team":"rr","mp":5,"won":2,"los":3,"pts":4},
    {"team":"dc","mp":6,"won":4,"los":2,"pts":8},
    {"team":"pkbs","mp":6,"won":2,"los":4,"pts":4},
]
dict=[]
l=[]
pts=[]
for data in iplpoints:
    if data not in dict:
        dict.append(data)
print("NO OF PARTICIPANTS IS:",len(dict))
for data in dict:
    l.append(data["team"])
    upp=list(map(lambda l:l.upper(),l))
print(upp)
for data in dict:
    pts.append(data["pts"])
    m=max(pts)
    if data["pts"]==m:
        print("TEAM WITH HIGHEST POINT",data)
for data in dict:
    mi=min(pts)
    if data["pts"]==mi:
        print("team with lowset points",data)
pi=[]
for data in iplpoints:
    pi.append(data["pts"])
p=list(sorted(pi))
print(p)
for i in range(0, 6):
    for data in iplpoints:
        if data["pts"] ==p[i]:
            print(data["team"])
            break















