#31/08/25
#cloe
#Assignment 3 option 1

# List of hours

hours = ["12pm", "1pm", "2pm", "3pm", "4pm", "5pm", "6pm"]

# empty  list to store temperaturs
temperature = []

# first step
'''for hour in hours:
    while True:
        try:
            temp = float(input(f"Enter temp for {hour} - "))
            temperature.append(temp)
            break      # exit loop if the person enters a invalid input
        except ValueError:
            print("please enter a valid number.")

# second step
Max_temp = max(temperature)  #highest temperature
Min_temp = min(temperature)  #lowers temperature

Max_index = temperature.index(Max_temp)   #find position
Min_index = temperature.index(Min_temp)

print()
print(f" Warmest was {Max_temp}°C at {hours[Max_index]}")
print(f" Coldest was {Min_temp}°C at {hours[Min_index]}")

average = sum(temperature) / len(temperature)   # find the avarage out of all the temperaturs
print(f"Average temperature: {average:.2f}°C")
'''

#Inputs

temp1 = float(input("Enter temp fot 12pm"))
temp2 = float(input("Enter temp fot 1pm"))
temp3 = float(input("Enter temp fot 2pm"))
temp4 = float(input("Enter temp fot 3pm"))
temp5 = float(input("Enter temp fot 4pm"))
temp6 = float(input("Enter temp fot 5pm"))
temp7 = float(input("Enter temp fot 6pm"))

#prosses

max = temp1
if(temp2>max):        # i asume its the first one but if its not reasine
    max = temp2

if(temp3>max):
    max= temp3

if(temp4>max):
    max = temp4

if(temp5>max):
    max = temp5

if(temp6>max):
    max = temp6

if(temp7>max):
    max = temp7

    # min
min = temp1
if(temp2<min):
    min = temp2

if(temp3<min):
    min = temp3

if(temp4<min):
    min = temp4

if(temp5<min):
    min = temp5

if(temp6<min):
    min = temp6

if(temp7<min):
    min = temp7
print()
print("The Coldest was,",max)
print()
print("The Warmest was,",min)


























