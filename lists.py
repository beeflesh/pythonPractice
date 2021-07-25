# fun lil string list
friends = ["Ayeola","Ryan","Kat","Josh"]
# list containing different types of values and its fine
test = ["Kevin",2,False]
# lets access elements in a list
# you can just print the list or
print(friends)
# you can call elements by index
print(friends[2])
print(test[1])
# you can also call elements by index from back of list
print(friends[-1]) # accesses last element
print(friends[1:]) # accesses elements at 1 and all after
print(friends[1:3]) # grabs elements starting at 1 UP TO (not including) element at 3
# we can also modify elements, not just access them.
friends[2] = "Kajaa" # changes element at index 2
print(friends)

# now lets talk about list functions
# lets say we have two lists:

bugs = ["beetle","ladybug","spider"]
luckyNums = [3,8,4,5,13]
print(bugs)
print(luckyNums)
# we can tack one onto the other using extend()
bugs.extend(luckyNums)
print(bugs)
#we can also just add individual elements to lists using append()
bugs.append("butterfly") #always adds item at end of the list
print(bugs)
#you can insert elements at a specific index using insert()
bugs.insert(1,"ant") #inserts "ant" at index 1, pushes other elements to the right
print(bugs)
#we can also remove elements
bugs.remove(3) #takes out the 3
print(bugs)

bugs.pop() #pops off last element
print(bugs)

print(bugs.index("ladybug")) #gives us the index of element, if you try with element
#that doesnt exist, throws error

bugs.append("ladybug") #so now since we just added another ladybug element,
#we can use the count() function to see how many ladybug elements we have

print(bugs.count("ladybug")) #returns the number of times ladybug is an element

#we can also sort lists
bugs.clear() #empties the list
print(bugs)
bugs = ["ladybug","spider","bee","beetle","fly"]
bugs.sort() #sorts the strings in alphabetical order, will not work if using different types
print(bugs)
luckyNums.sort() #sorts numbers in ascending order
print(luckyNums)

#we can also reverse lists
luckyNums.reverse()
print(luckyNums)

#we can also copy entire lists
bugs2 = bugs.copy()
print(bugs2)
print(bugs)
