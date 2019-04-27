#Robert Bangiyev
#October 23, 2018
#Does greetings by the hour
time=int(input("Enter hour (in 24 hour time): "))
if(time<12):
    print("Good Morning")
elif(time>=12 and time<17):
    print("Good Afternoon")
else:
    print("Good Evening")
