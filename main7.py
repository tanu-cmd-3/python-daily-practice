marks=[93.0 ,98.3 ,98.4 ,87.5, 75.9,"tanu"]
print(len(marks))
print(marks[4])
print(marks[0])
print(marks[5])
marks[3]='tanuja'
print(marks)
print(marks[0:4])#ending index is not included
print(marks[-3:-1])
list = [2,1,3]
list.append(4)
print(list)
print(list.sort())#gives none
print(list)#returns ascending values
list.sort(reverse = True)
print(list)
list1=['bananna','apple','mango']
list1.sort()#strings are sorted based on chars
print(list1)
list1.reverse()#reverses the sorting
print(list1)
list1.insert(1,'kiwi')#list1.insert(index,element to be inserted)
print(list1)
list1.pop(2)
print(list1)