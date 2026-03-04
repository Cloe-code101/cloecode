#17/09/2025


import random
import time

print("What is your name stranger?")                 # asking the name
                                                         
Name = input()
       
print(f"Hello {Name} welcome to the magic 8 ball") # welcoming
print()
print("Loading....")
time.sleep(3)
print("I am your fortune cookie today")
print()
print("loading....")
time.sleep(3)
print("Think about your luck today and in your head give yourself a question i will respond it with magic🪄🪄")
time.sleep(5)
print("3")
time.sleep(2)
print("2")
time.sleep(2)
print("1")
time.sleep(2)
print("Ah i have your fortune")
time.sleep(3)
print("I found it")
print()
number = (random.randint(1, 30))            #mystery number chosen

if number >=1 and number<=10:             #checking the number in range 
    print(f"Oh no {Name} your fornune and luck is out for the day ☠")

elif number >=11 and number<=30:
    print (f"OMG 🤯 {Name} your luck 🍀 is incredible i advise you to buy a lotery card!!!")
    

