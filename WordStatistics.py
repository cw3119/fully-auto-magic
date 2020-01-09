#Word Statistics
import string
name= input("Enter the file:")
file = open(name,'r')
words=[]
sentanceCount=0
for line in file:
    splitWords= line.split()
    for x in splitWords:
        
        x.lower()
        if x[-1] ==".":
            sentanceCount+=1 

        x.strip(".")
        words.append(x)


wordSet=set(words)
totalLetters=0
averageLength=0
for x in words:
    totalLetters+= len(x)

averageLength=totalLetters/len(words)        


print("Total Words: ", len(words))

print("Unique Words ", len(wordSet))

print("Average word length:", averageLength)

print("Number of sentences:", sentanceCount)

