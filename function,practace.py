def Calculate(n1,n2,symbol):  #function
    if(symbol == "+"):      #the if is comparing the symbols
        print(n1 + n2)
    if(symbol == "*"):
        print(n1 * n2)
    if(symbol == "-"):
        print(n1 - n2)
    if(symbol == "/"):
        print(n1 / n2)

    
n1 = int(input())    #getting inputs from the users
n2 = int(input())
symbol = input()

Calculate(n1,n2,symbol)  #call the function

