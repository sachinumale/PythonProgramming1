from functools import reduce
'''
#1 Addition of tow no:
s=lambda a,b:a+b
print(f"Addition of {3}+{2}:",s(2,3))
'''


'''
#2 Find biggest of two no

result=lambda a,b: a if a>b else b

print(f"from {1} and {4} bigger no is:",result(1,4))
'''
'''
#3 Lambda function to find biggest 3 numbers?

result= lambda a,b,c: a if a>b and a>c else b if b>c else c

print(f"from {9},{4} & {8} biggest no is:", result(9,4,8) )
'''
'''----------------------------------------------------------------------------------------------------'''
#filter
#map
#reduce

#1. filter(finction, sequence)
#WAP to filter only even numbers from the list by using filter() function?
'''
def sort(n):
    return n%2==0
l1=[1,2,3,45,6,7,8,9]

data=list(filter(sort,l1))
print(data)
'''

# with lambda function
'''
#s=lambda n:n%2==0
l1=[1,2,3,4,5,66,6,8]
data=list(filter(lambda n:n%2==0,l1))
print(data)
'''

#------------------------------------------------------------------------------------------------
#map():
'''
def double(n):
    return 2*n
#Without lambda function
l1=[2,4,6,8,10]
data=list(map(double,l1))
print(data)
'''
'''
#With lambda function

l1=[1,2,3,4,5,6,7,8,9]

data=list(map(lambda n: n*2,l1))
print(data)
'''

#reduce() : Find sum of all employee salaries

emp=[1,2,3,4,5,6,7,8,9]
data=reduce(lambda x,y:x+y,emp)
print(data)

