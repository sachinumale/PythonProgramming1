class Student:

    def __init__(self,ename,ecity,esal):
        self.ename = ename
        self.ecity = ecity
        self.esal = esal

    def display(self):
        print("Employee updated salary is: ",self.esal)



class Salary:
    @staticmethod
    def increment(sal):
        sal.esal = sal.esal + 4000
        #Student.display(sal)
        sal.display()


s = Student("Shrikrushna","Pune",56000)
Salary.increment(s)
