#class which is declared inside other class
#When we should go for Inner Classes --> Without creating one type of object, there is no chance fo create another object

class Test:
    def __init__(self):
        print("This is main class")

    class Inner:
        def __init__(self):
           print("This is Inner class")

        def m1(self):
           print("This is Inner class method")

        class InInner:
            def __init__(self):
                print("This is In-Inner class")

            def m2(self):
                print("This is In-Inner method")

m = Test()
i = m.Inner()
i.m1()
iI= i.InInner()
iI.m2()
