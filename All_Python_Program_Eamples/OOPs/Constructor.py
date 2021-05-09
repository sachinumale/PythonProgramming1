class Test():
    def __init__(self,x,y):
        self.name = x
        self.surmane = y
        # print("Name of Customer is: ", self.name)   call constructor explicitly
        # print("Name of Customer is: ", self.surmane)  call constructor explicitly

    def customer_name(self):
        print("Name of Customer is: ",self.name)
        print("Name of Customer is: ", self.surmane)


t = Test("Shrikrushna","Khedkar")
t.customer_name()

# t.__init__("Ghuge","Sonali") call constructor explicitly
# print(t.name)  call constructor explicitly
# print(t.surmane)  call constructor explicitly