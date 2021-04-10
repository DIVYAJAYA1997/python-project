class Student_details:
    def __init__(self,name,course,total,marks):
        self.name=name
        self.course=course
        self.total=total
        self.marks=marks
    def __str__(self):
        return self.name
obj=Student_details("Divya","b.tech",1234,100)
obj1=Student_details("Athulya","mca",4567,150)
obj2=Student_details("Sherlin","mca",6789,200)
obj3=Student_details("Arathi","b.tech",7567,120)
l=[]
l.append(obj1)
l.append(obj)
l.append(obj2)
l.append(obj3)
student=list(map(lambda st:st.name.upper(),l))
print(student)
marks=list(map(lambda sd:sd.marks+50,l))
print(marks)
num=[2,4,3,6,7]
even=list(filter(lambda n:n%2==0,num))
print(even)
names=["arathi","anett","arya","vani","divya"]
name=list(filter(lambda n:n[0]=="a",names))
print(name)
course=list(filter(lambda c:c.course=="mca",l))
for std in course:
    print(std)
course=list(map(lambda st: st.name,list(filter(lambda c:c.course=="mca",l))))
print(course)
maximum=max(list(map(lambda std:std.total,l)))
print(maximum)
minimum=min(list(map(lambda n:n.total,l)))
print(minimum)

