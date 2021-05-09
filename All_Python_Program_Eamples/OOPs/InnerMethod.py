class Test:
    def MainMethod(self):

        def m1(a,b):
            print("Addition of two no is:", a+b)
            print("Subastrctation of two number is:", a-b)
            print("Division of two are is:",a/b)
            print("Miltiplication of two no is:",a*b)
            print()

        m1(3,2)
        m1(30,20)
        m1(300,200)

t = Test()
t.MainMethod()