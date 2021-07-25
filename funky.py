# now lets talk about functions
# functions are portions of code that do a specific task (like methods in java)
# here we define a function and give it a name
# everything after the : describes the functions behavior
# we must indent after this colon
def greetings():
    # code indented here is in the function
    print("hey you")
# code not indented is NOT in the function

# now that weve described a function, we have to call it to use it:
greetings()
# generally functions in python are all lowercase and words are separated by _

# we can also define functions that need parameters
def greet(name):
    print("hey "+name)

#then we call it and pass a parameter
greet("Bee")



