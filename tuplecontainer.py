# tuple is a structure where we can store multiple pieces of information
# similar to a list but a little different

coordinates = (4,5) #use () instead of [] to make a tuple. [] makes a list.
#tuples are immutable (cannot be changed or modified)
#if you try to reassign values in tuple, python will throw error

print(coordinates[0]) #can call an element at an index using []

#in practical use, you use tuple for data that never changes (think final)

#we CAN create a list of tuples and change those values

coordinates2 = [(4,5),(6,7),(80,34)]
print(coordinates2)
coordinates2[1] = (3,2)
print(coordinates2)

