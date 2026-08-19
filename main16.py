marks={}
x=int(input("Enter marks of phy: "))
marks.update({"phy": x})

y=int(input("Enter marks of chem: "))
marks.update({"chem": y})

z=int(input("Enter marks of bio: "))
marks.update({"bio": z})
print(marks)