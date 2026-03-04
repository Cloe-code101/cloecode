



print("Enter your age [18-50 only]:")
Age = int(input())

while (Age <18 or Age>50):
    print("Invalid age. 18-50 omly allowed.")
    Age = int(input())
    print(Age, "is valid")