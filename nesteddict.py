students={
    1000:{"id":101,"name":"divya","course":"developer","qualification":"btech"},
    1001:{"id":102,"name":"arathy","course":"developer","qualification":"btech"},
    1002:{"id":103,"name":"sherlin","course":"developer","qualification":"btech"}
}
id=int(input("ENTER THE ID:  "))
property=input("ENTER THE PROP U WANT TO DISPLAY:")
if id in students:
    print(students[id])
    if property in students[id]:
        print(students[id][property])
    else:
        print("invalid property")
else:
    print("not exist")


def details(**kwargs):
    id=kwargs["id"]
    prop=kwargs["course"]
    if id in students:
        print(students[id]["name"])
        if prop in students:
            print(students[id]["course"])
        else:
            print("invalid")
    else:
        print("NOT EXIST")




