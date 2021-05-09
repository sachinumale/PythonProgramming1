
def fact(n):
    result =1
    while n>1:
        result = result * n
        n=n-1
    return result

# a1=fact(5)
# print(a1)
i = int(input("Enter factorial no: "))
for f in range(i+1):
    print(f"Factorial of number {f} is : {fact(f)}")

#-----------------------------------------------------------------------------

# Using Recursion method

# def fact(n):
#     if n==0:
#         total =1
#     else:
#         total=n*fact(n-1)
#     return total
#
# print(fact(10))