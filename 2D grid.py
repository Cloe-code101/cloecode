#14/01/2026
# cloe
# 2D array


# first step

stats= [[0,0,12,45,20,51,23],       #sun          
        [18,23,432,423,64,34,54],   #mon        
        [11,8,63,45,60,234,432],    #tue
        [23,84,68,55,64,454,452],  #wed
        [0,0,34,65,98,456,821],     #thur
        [0,0,0,6,3,0,0],            # fri
        [0,0,0,0,5,4,2]             #sat
        
]

DaysofWeek = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saterday"]
TimeofDay = ["12PM","1PM","2PM","3PM","4PM","5PM","6PM"]

# step 2 print
#print(stats)

# make it cube

for row in range(7):
    for col in range(7):
        print(stats[row][col], end = " ")
    print()
    
# 4
MaxDay=0
MaxHour=0

for day in range(7):
    for hour in range(7):
        if(stats[day][hour]>stats[MaxDay][MaxHour]):
            MaxDay = day
            MaxHour = hour
            
            
print("The busiest day is", DaysofWeek[MaxDay], "at", TimeofDay[MaxHour])
            


















