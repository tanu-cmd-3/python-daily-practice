marks=82
if(marks>=90):
    grade='A'
elif(marks>=80 and marks<90):
    grade='B'
elif(marks>=70 and marks<80):
    grade='C'
else:
    grade='D'
print("Grdae of the student is->",grade)
#nesting
age= 68

if(age>=18):
    if(age>=80):
        print('cannot drive')
    else:
        print("can drive")
else:
    print("Cannot drive")

num=int(input("Enter a number: "))
if(num%2==0):
    print("The number is even")
else:
    print("The number is odd")