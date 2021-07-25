from math import * #needed to import math functions

print("Hello World")
print("    /|")
print("   / |")
print("  /  |")
print(" /___|")
#python executes in order
#now lets talk about variables
character_name = "George"
character_age = 70

print("There once was a man named "+character_name+", ")
print("he was "+str(character_age)+" years old.")
print("He really liked the name "+character_name+", ")
print("but didn't like being "+str(character_age)+".")

character_name = "John"

print("There once was a man named "+character_name+", ")
print("he was "+str(character_age)+" years old.")
print("He really liked the name "+character_name+", ")
print("but didn't like being "+str(character_age)+".")
#string methods:

#some escape sequences similar to java: \n \" \\
phrase = "super bugs"
print("Big \"Bugs\"\nknow hugs")
print(phrase+" are strong")
#functions are to python as methods are to java
#functions, blocks of code that runs and does something for us
print(phrase.lower()) #makes the string lowercase
print(phrase.upper()) #makes the string uppercase
print(phrase.isupper()) #will return true if entirely uppercase (boolean function)
print(phrase.upper().isupper()) #will return true cause you're making it all
#upper case and then checking to see if uppercase
print(len(phrase)) #length function to check length of string
print(phrase[0]) #grabs character at given index (0 is start)
print(phrase.index("p")) #shows index value of given character or string
print(phrase.index("bug")) #will show index of the start of this string
#if you use a string/character that isnt in the string, it will throw error

print(phrase.replace("bugs","hugs")) #replaces given character or string with what
#you specify

myNumber = -5
print(myNumber)
#before you can concatenate a number and a string, you must typecast it as string
#with str()
print(str(myNumber)+" is my number.")
print(abs(myNumber)) #shows absolute value with abs()
print(pow(myNumber,2)) #raises a number to a power (-5^2 in this example)
print(max(5,7)) #will return larger number between the two
print(min(5,7)) #will return smaller number between the two
print(round(3.2)) #will round down if under .5, will round up if above .5

#Now we should import math
print(floor(3.7)) #rounds down no matter what
print(ceil(3.7)) #rounds up no matter what
print(sqrt(36)) #returns square root

#getting input from users

name = input("Enter your name: ") #prompt is in (), then the input is stored into name
age = input("Enter your age: ")
print("Hello "+name+"! You are "+age)










