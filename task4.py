employees=[
    ["id101","VANI","developer",20000,1990,1997],
    ["id103","BANI","programmer",30000,2001,2006],
    ["id102","JAY","developer",20000,2000,2009],
    ["id104","VIBHA","testing",35000,1997,2016],
    ["id105","MEERA","programmer",30000,1990,2000]
]
flag=0
for data in employees:
    if data[4]==1990:
        print(data[1])
    elif data[5]==1990:
        print(data[1])
        flag=0
    else:
        flag=1
exp=[]
for data in employees:
    exp.append(data[5]-data[4])
print(exp)
print(max(exp) ,"is the max experience")
for data in employees:
    if data[5]-data[4]==max(exp):
        print(data[1],"has max expereience")
        break





