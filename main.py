# Write your pseudocode first!
import pyperclip
import random
#dict for web:passsword
Webster = {

}
aniya = "y"
while aniya == "y" :
    Symbols = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=_+[],./<>?:;'"

    #ask user for password
    x = input("What website would you like to add? ")
    print(" ")
    #create password
    random_Symbols = ""
    for i in range(7):
        random_Symbols += random.choice(Symbols)
    #showing password
    print("Here's your password:", random_Symbols)
    #add to dict
    Webster[x] = random_Symbols
    #pyperclip
    pyperclip.copy(random_Symbols)



    #while loop
    aniya = input("Would you like to add another password? (y/n) ")

print("\nYour passwords: ")
for x,random_Symbols in Webster.items():
    print(f"{x} : {random_Symbols}\n")
print("You ended the program.")