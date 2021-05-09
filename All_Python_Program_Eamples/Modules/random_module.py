from random import *
print("1. random(): float value from 0 t0 1")
print("-"*20)
#1. random(): float value from 0 t0 1

for x in range(10):
    print(random())
print("*"*40)
#2. randint: int value
print("2. randint: int value")
print("-"*20)
for x in range(10):
    print(randint(2, 100))
print("*"*40)
#uniform: To generate random float value in the given range.
print("3. uniform: To generate random float value in the given range.")
print("-"*30)

for x in range(10):
    print(uniform(1,100))
#---------------------------------------------------------------
print("*"*40)
print("4. randrange():")
print("-"*10)

for x in range(10):
    print(randrange(1,100,2))

#---------------------------------------------------------------
print("*"*40)
print("5. choice: It returns a random object from the given sequence like list or tuple")
print("-"*30)
names=["Pune","Beed","Mumbai","Aurangabad","Nagpur"]
for x in range(10):
    print(choice(names).upper())
