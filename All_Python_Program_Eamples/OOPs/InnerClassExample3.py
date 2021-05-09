class Car:
    def __init__(self,name):
        print("Car object has been created")
        self.name = name
        self.engin = self.Engin()

    def display(self):
        print("Name of the car is: ", self.name)
        print("Car has following specification:")
        self.engin.m1()
        self.engin.color.m2()


    class Engin:
        def __init__(self):
            print("Engin object has been created")
            self.color = self.Color()
        def m1(self):
            print("1. Turbo with 4 stroke booster engine ")

        class Color:
            def __init__(self):
                print("Color object has been created")
            def m2(self):
                print("2. Dark blue with teflon coating")


c = Car("Honda")
c.display()
# e1 = c.Engin()
# cc = e1.Color()