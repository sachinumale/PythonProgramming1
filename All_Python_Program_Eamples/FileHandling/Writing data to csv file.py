#Writing data to csv file:

import csv

f=open("test.csv","w",newline="")
w=csv.writer(f)
w.writerow(["Eno","Ename","Esal","Eadd"])

while True:
    enum=int(input("Enter Employee No: "))
    ename = input("Enter Employee Name: ")
    esal = int(input("Enter Employee Salary: "))
    eaddress = input("Enter Employee Address: ")
    w.writerow([enum,ename,esal,eaddress])
    option = input("Want to add one more record [Yes|No]: ").lower()
    if option not in["y","yes"]:
        option=input("Kindly provide correct input [Yes|No]: ").lower()
    elif option not in ["no","n"]:
        break
f.close()
print("Data saved successfully")