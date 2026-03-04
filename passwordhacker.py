#03/09/25
#cloe
# password haker

password = "P@SW0RD"

tries = 0

Maxtries = 3

while tries < Maxtries:
    attempt = input("Enter the password: ")
    if attempt == password:
        print("🔓 Access Granted!")
        break
    else:
        print("❌ Incorrect.")
    else:
        print("nice job hacker")
