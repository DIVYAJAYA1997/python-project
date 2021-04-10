def add(a,b,c):
    return a+b+c

def add(num1,num2):
    return num1+num2

add(1,3)

def func(*num):
    print(num)

func(10,20,30)
func(20,50,60,70,30)

def star(**num):
    print(num)

star(id=123,name="asdfg",job="developer")


def student_details(**num):
    print(num)

student_details(rollno=1,name="veena",std=1)
