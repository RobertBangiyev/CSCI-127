#Name: Robert Bangiyev
#Date: October 9, 2018
#This program counts the number of plurals the user inputs
message=input("Enter nouns: ")
num=message.count(" ")
plurals=message[:-1].split(" ")
wordcount=len(plurals)
pluralcount=0
for i in plurals:
    if(i[len(i)-1:len(i)]=="s"):
        pluralcount+=1
if(message[len(message)-1:len(message)]=="s"):
    pluralcount+=1
print("Number of words: ", wordcount)
if(pluralcount==0):
    print("Fraction of your list that is plural is ", float(0))
else:
    print("Fraction of your list that is plural is ", (float(pluralcount)/float(wordcount)))
