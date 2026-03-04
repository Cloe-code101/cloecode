#27/08/25
#challenge 2
#cloe and lara

print("Please enter the scores of the 8 students")

 #this is for the value of each student

Student1 = int(input())

Student2 = int(input())

Student3 = int(input())

Student4 = int(input())

Student5 = int(input())

Student6 = int(input())

Student7 = int(input())

Student8 = int(input())

sum = (Student1) + (Student2) + (Student3) + (Student4) + (Student5) + (Student6) + (Student7) + (Student8)
avg = sum/8
print(Student1, "+", Student2, "+", Student3, "+", Student4, "+", Student5, "+", Student6, "+", Student7, "+", Student8, "=", sum)
print()
print("The average is")
print()
print(avg)

count = 0

if(Student1 >40):
    count = count + 1

if(Student2 >40):
    count = count + 1

if(Student3 >40):
    count = count + 1

if(Student4 >40):
    count = count + 1

if(Student5 >40):
    count = count + 1

if(Student6 >40):
    count = count + 1

if(Student7 >40):
    count = count + 1

if(Student8 >40):
    count = count + 1


print( count )




