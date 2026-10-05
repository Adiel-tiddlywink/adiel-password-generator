# Write your pseudocode first!
import pyperclip
import random
#dict for web:passsword
Webster = {

}

#symbols
Symbols = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=_+[],./<>?:;'"

#ask user for password
x = input("What website would you like to add? ")



#create password
random_Symbols = ""
for i in range(7):
    random_Symbols += random.choice(Symbols)

#add to dict
Webster[random_Symbols] = Webster



#pyperclip




#print dict




#input password^2