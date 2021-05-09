import csv

f1=open("test.csv","r")
re=csv.reader(f1)
data=list(re)
for x in data[0]:
    print(x,"\t\t",end="")
print()
print("-----------------------------------------------")
for x in data[1:]:
    row=int(x[2])
    if row < 2500:
        for valu in x:
            print(valu,"\t\t",end="")
        print()

f1.close()