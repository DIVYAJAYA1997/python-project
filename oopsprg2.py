class Student:
    cname="SBCEW"
    def student_details(self,name,course):
        self.name=name
        self.course=course

    def print_details(self):
        print(self.name)
        print(self.course)
        print(self.cname)

obj1=Student()
obj1.student_details("DIVYA","b.tech")
obj1.print_details()
print(obj1.name)
print(Student.cname)
