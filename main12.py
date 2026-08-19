student={"name":"tanuja",
         "subjects":{
             "phy":98,
             "chem":95,
             "bio":100
         }
}
#print(student["name2"])#error
print(student.get("name2"))#no error
new={"name":"Tanu","city":"Bengaluru","age":21}
student.update(new)
print(student)