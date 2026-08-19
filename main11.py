#dictionary and sets
info = {
    "key":"value",
    "name":("Tanu","Jhon","David"),
    "learning":"Tanu",
    "age":22,
    True:94.4
}
info["name"]="shraddha"
print(info["name"]) 

#nested dictionary
student={"name":"Tanuja",
         "subjects":{
             "phy":80,
             "chem": 90,
             "bio":100,
             "maths":89
             },
        "rollno":71,
        "USN":"2VD23CS080"
        }
print("These values comes under nested dictionary->\n",student["subjects"]["phy"])
print(list(student.keys()))#type casting
print(len(list(student.keys())))#returns keys
print((student.values()))#returns all values
print(list(student.values()))
pairs=list(student.items())#returns all key-value pairs in list form
print(pairs[0])
