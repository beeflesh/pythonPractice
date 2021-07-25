#okay, so for funsies lets do a mad libs

#first, im going to write up a little story that can have elements replaced

#it might go something like:
#Dear Jim, Its been a long time since I've seen, I hope you are doing well. I picked up some bread from the bakery
#the other day and it was stale when I bought it! I couldn't believe it so I walked back in to make sure I didn't make
#a mistake and pick up old bread. I asked the clerk if he had any fresh bread and he told me that they hadn't
#had fresh bread in days. He looked so ashamed!

# Now that we have a little story, let's take out the pieces that a user can alter:
# Dear {proper_noun}, Its been a long time since I've {verb past tense}, I hope you are {verbing} {adjective}. I {verb past tense}
# up some {noun} from the bakery the other {unit of time} and it was {adjective} when I bought it! I
# couldn't believe it so I {verb past tense} back in to make sure I didn't make a mistake and pick up {adjective} {noun}.
# I {verb past tense} the clerk if he had any {adjective} {noun} and he told me that they hadn't
# had {adjective} {noun} in {unit of time}. He looked so {adjective}!

#now that we've split up what we want to change into managable bits, lets prompt the user to replace some of these.

proper_noun = input("Enter a proper noun: ")
verbPast = input("Enter a past tense verb: ")
verbing = input("Enter a verb ending in ing: ")
adj = input("Enter an adjective: ")
verbPast2 = input("Enter a past tense verb: ")
noun = input("Enter a noun: ")
unitOfTime = input("Enter a unit of time: ")
adj2 = input("Enter an adjective: ")
verbPast3=input("Enter a past tense verb: ")
adj3 = input("Enter an adjective: ")
noun2 = input("Enter a noun: ")
verbPast4 = input("Enter a past tense verb: ")
adj4 = input("Enter an adjective: ")
noun3 = input("Enter a noun: ")
unitOfTime2 = input("Enter a unit of time: ")
adj5 = input("And finally, one more adjective: ")

#now we just slip these variables into the prompt and print it

print("Dear "+proper_noun+",\nIts been a long time since I've "+verbPast+", I hope you are "+verbing+" "+adj+".\nI "+verbPast2+" up some "+noun+"s from the bakery the other "+unitOfTime+" and they were "+adj2+" when I bought them!\nI couldn't believe it so I "+verbPast3+" back in to make sure I didn't make a mistake and pick up a "+adj3+" "+noun2+".")
print("I "+verbPast4+" the clerk if he had any "+adj4+" "+noun3+"s and he told me that they hadn't\nhad "+adj4+" "+noun3+"s in "+unitOfTime2+"! He looked so "+adj5+"!")


