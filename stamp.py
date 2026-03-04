
#- Has 4 arrays called --> Country, Value, Year Issued and Quality (1-3. 1 means poor condition and 3 means excellent condition)
#- Allows Jake to enter data for each stamp into the array using a WHILE loop.
#- Prints out all the information using a Pretty Table once the entries are done.
#- Sorts the data by country name using a Bubble Sort and displays the sorted list.

# empty lists

Country = []

Value = []

Year = []

Quality = []

country = input("Enter country (Say stop to stop the loop)")

while country != "stop":
    Country.append(country)

    Value.append(input("Value: "))

    Year.append(input("Year: "))


    q = input("Quality (1-3): ")
    while q < "1" or q > "3":

        print("Enter 1, 2, or 3 only!")

        q = input("Quality (1-3): ")

    Quality.append(q)
    print()
    country = input("Country (Remember stop to end): ")

print("Countries:", Country)
print()
print("Values:", Value)
print()
print("Years:", Year)
print()
print("Qualities:", Quality)