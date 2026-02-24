#function body

def countWordLen(WordList,num):
    counter = 0 # keeping track of the words
    # loop
    
    for i in range(0, len(WordList)):
        if(len(WordList[i])>=num):
            counter = counter + 1
    #end of loop
    return counter
#end

# caling the function

print(countWordLen(["Sun","Tree","Book","Wind","Candle","Mirror"],4))

# chalange

def displayContacts(contactList,letter):
    emptyList = []
    
    for i in range(len(contactList)):
        if(contactList[i][0].lower()==letter.lower()):
            emptyList.append(contactList[i])
        
    return emptyList

print(displayContacts(["Liam", "Emma", "Noah", "Ava", "Jake", "Mia", "Jack", "John"], "J"))




















