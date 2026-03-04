#24/08/25
#cloe
#homework

name = input("Enter your name")
birth_year = int(input("Enter you year of birth: "))

age = 2025 - birth_year #because the current year is 2025

if age < 0 or age > 100:
    print("Invalid age, Please enter a valid year of birth")
else:
    if age < 18:
        years_left = 18 - age
        print("Sorry,", name + ", you are not old enough to vote")
        print("You can vote in", years_left, "years.")
    else:
        years__voting = age - 18
        print("Hi", name + ", you can vote!")
        print("You have been able to vote for", years__voting, "years.")