class Test():

    collegeName = "ABC"  # Static variable

    def __init__(self,name,rollno):     #Consttructor
        self.name=name      # Instance variable
        self.rollno=rollno


    def getStudent(self):       #Instance method
        print("Name of Student:", self.name)
        print("Roll no of Student:",self.rollno)

    @classmethod
    def getSchool(cls):        # Class method
        print("Name of the College is:",cls.collegeName)

    @staticmethod
    def getAvgMark(a,b):    # Static method
        sum1= a+b
        return sum1


t=Test("Shrikrushna",11)
t.getStudent()      # object to call instance method
Test.getSchool()   # object to call class method
total=Test.getAvgMark(10,20) # object to call static method
print("Addition of ",total)
