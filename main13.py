#sets
collection={1 ,2 ,2, 3 ,3 ,4 ,5,"hello","world" }#ignores the duplicate values
print(collection)#sets are unordered i.e the output order will change after every run
print(type(collection))
print(len(collection))#ignores duplicate value

empty={}
print(type(empty))#gives class as dict not set
empty1=set()
print(type(empty1))#gives class as set

collection.add((6,7,8,9))#hashable
#collection.add({6,7,8,9})#unhashable
#collection.add([6,7,8,9])#unhashable
print(collection)

collection.remove(2)
print(collection)

sets={3,4,5,"hello"}
print(len(sets))
sets.clear()
print(len(sets))

sets1={"hello","apna-college", 3, 6, "good", "better", 90, "great"}
print(sets1.pop())#pops random value from given sets1