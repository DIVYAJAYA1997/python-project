num1=int(input("ENTER NUM1:"))
num2=int(input("ENTER NUM2:"))
try:
    result=num1/num2
    print(result)
except Exception as a:
    print(a.args)
    num2 = int(input("ENTER NUM2:"))
    try:
        result=num1/num2
        print(result)
    except Exception as e:
        print(e.args)
finally:
    print("COMPLETED")
    print("1234567,...")