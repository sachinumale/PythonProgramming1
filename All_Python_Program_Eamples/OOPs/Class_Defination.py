class Student():

    def __init__(self,name,age,mark):
        self.name = name
        self.age = age
        self.mark=mark

    def get_data(self):
        print("Student Name is: ", self.name)
        print("Student age is: ",self.age)
        print("Student Mark is: ",self.mark)

s = Student("Shri",30,90)
s.get_data()
print("-"*40)
s1 = Student("Khedkar",28,80)
s1.get_data()