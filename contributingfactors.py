#Robert Bangiyev
#October 23, 2018
#Lists top 3 contributing factors
import pandas as pd
filename=input("Enter CSV file name: ")
data=pd.read_csv(filename)
print("Top three contributing factors for collisions: ")
print(data["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3])
