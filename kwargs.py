students={
    1000:{"id":101,"name":"divya","course":"developer","qualification":"btech"},
    1001:{"id":102,"name":"arathy","course":"developer","qualification":"btech"},
    1002:{"id":103,"name":"sherlin","course":"developer","qualification":"btech"}
}
def student_details(**kwargs):
    id=kwargs["id"]
    course=kwargs["course"]
    if id in students:
        print(students[id])
        if "course" in students[id]:
            print(students[id]["course"])
        else:
            print("invalid")
    else:
        print("INVALID")
student_details(id=1000,course="course")

