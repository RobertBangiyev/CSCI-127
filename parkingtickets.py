#Robert Bangiyev
#October 23, 2018
#Finds 10 worst offences in category
import pandas as pd
namefile=input("Enter file name: ")
attribute=input("Enter attribute: ")
tickets=pd.read_csv(namefile)
print("The 10 worst offenders are:")
print(tickets[attribute].value_counts()[:10])
