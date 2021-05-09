from random import *
alphabets = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
cities = ['Hyderabad', 'Chennai', 'Bangalore', 'Pune' , 'Delhi', 'Mumbai' ]
designations = ['Software Engineer', 'Senior Software Engineer', 'Team Lead', 'Project Lead' , 'Project Manager']

'''
1. The name should contains 3 to 10 Characters
2. First Character should be upper case and remaining characters should be lower case
'''
def get_fake_emp_name():
    n = choice(alphabets).upper()
    p1=randint(2,9)
    print(p1)
    for x in range(p1):
        n=n+choice(alphabets)
    return n
#Employee Number should starts with “e-” followed by 4 digits
#eg: e-1234

def get_fake_emp_no():
    n1= 'e-'
    for x in range(4):
        n1=n1+choice(digits)
    return n1


#Employee Salary should be float value from 10000 to 50000

def get_fake_emp_salary():
    p1=uniform(10000,50000)
    return p1

#Employee City Should be from:[‘Hyderabad’, ’Chennai’, ‘Bangalore’, ‘Pune’ , ‘Delhi’, ‘Mumbai’ ]

def get_fake_emp_city():
    city= choice(cities)
    return city

#Mobile Number should contains exactly 10-digits where first number should be 6 to 9.
#No restriction on remaining digits.
#  eg:  9848098480

def get_fake_emp_mob():
    mob=choice('6789')
    for x in range(9):
        mob=mob+choice(digits)
    return mob

#Employee Designation Should be from:[‘Software Engineer’, ‘Senior Software Engineer’, ‘Team Lead’, ‘Project Lead’ , ‘Project Manager’]

def get_fake_emp_destination():
    desti=choice(designations)
    return desti


def get_emp_data():
    print("Employee name is: ",get_fake_emp_name())
    print("Employee number is:", get_fake_emp_no())
    print("Employee salary no is:",get_fake_emp_salary())
    print("Employee city is:",get_fake_emp_city())
    print("Employee mob no is:",get_fake_emp_mob())
    print("Employee destination is:",get_fake_emp_destination())

data=eval(input("Enter no of employee data required: "))
for x in range(data):
   print("-"*40)
   print(f"Employee data no {x+1}: ")
   get_emp_data()





