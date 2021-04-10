dict={"id":120,"name":"VIBHA","t":250}
print(dict)
dict["id"]=200
print(dict["id"])
print(dict)
if "gender" in dict:
    print("it exists")
else:
    dict["gender"]="female"
print(dict)
dict["t"]+=50
print(dict["t"])