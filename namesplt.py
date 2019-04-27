#Robert Bangiyev
#October 23, 2018
#Organize names
names=str(input("Please enter your list of names: "))
nlist=names.split(";")

for i in nlist:
    nems=str(i)
    qname=nems.split(",")
    for i in range(1):
        print(qname[1]+qname[0])
