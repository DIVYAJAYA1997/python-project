class Employee:
    def __init__(self,id,name,desig,exp,sal):
        self.id=id
        self.name=name
        self.desig=desig
        self.exp=exp
        self.sal=sal
    def __str__(self):
        return self.name
emplst=[]
f=open("employees","r")
for lines in f:
    id,name,desig,exp,sal=lines.rstrip("\n").split(" ")
    emplst.append(Employee(id,name,desig,exp,sal))
highsal=max(map(lambda emp:emp.sal,emplst))
print(highsal)

