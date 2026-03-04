#lists1.py
#09.23.2025
#cloe
# a program to make a small list to hold temperatures

t = 0

tempsData = [] # empty list
dayTimeList = [ "Mon 9AM", "Mon 9PM", "Tue 9AM", "Tue 9PM", "Wed 9AM", "Wed 9PM"]

# now we do a loop that will accept 6 temps

for temp in range(0,6):
    v = float(input(dayTimeList[temp]))
    tempsData.append(v)

print(tempsData)

# finding the avarage

for temp in range(0,6):
    t = t + tempsData[temp]

print(t/6)

# max and min

Max = tempsData[0]
Min = tempsData[0]

