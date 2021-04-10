class Student_details:
    def __init__(self,name,course,total):
        self.name=name
        self.course=course
        self.total=total
obj=Student_details("Divya","b.tech",1234)
obj1=Student_details("Athulya","mca",4567)
obj2=Student_details("Sherlin","mca",6789)
obj3=Student_details("Arathi","b.tech",7567)
l=[]
l.append(obj1)
l.append(obj)
l.append(obj2)
l.append(obj3)
t=[]
for ele in l:
    if ele.course=="mca":
        print(ele.name)
    else:
        break
for ele in l:
    t.append(ele.total)
print(max(t),"is the maximum total value")

