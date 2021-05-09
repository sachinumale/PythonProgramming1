class Student:

    def __init__(self,name,mark):
        self.name = name
        self.mark = mark

    def display(self):
        print('Name is:',self.name)
        print("Mark is:",self.mark)

    def grade(self):
        if self.mark > 60:
            print("Your are First class")
        elif self.mark > 50:
            print("You are Second class")
        elif self.mark > 35:
            print("You are Third class")
        else:
            print("You are Failed")

students = []
n = int(input("No of students:"))
for i in range(n):
    name = input("Enter student name:")
    mark = int(input("Enter student mark:"))
    s = Student(name,mark)
    students.append(s)

for student in students:
    student.display()
    student.grade()
    print()


