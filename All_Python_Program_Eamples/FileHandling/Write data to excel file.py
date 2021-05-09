import openpyxl
import os
from openpyxl import Workbook

wb = Workbook()
excel_sheet=wb.active
excel_sheet.append(["Eno","Ename","Esal"])
while True:
    eno=input("Enter Employee No: ")
    ename= input("Enter Employee Name: ")
    esal = input("Enter Employee Salary:")
    excel_sheet.append([eno,ename,esal])
    option=input("Want to add more employee data[Yes|No]:").lower()
    if option in ["no","n"]:
        break
    elif option not in ["yes","y"]:
        option=input("Kindly Enter Valid Input[Yes|No]: ")

os.getcwd()
wb.save("testExcel.xlsx")
print("Excel Data Save Successfully")