class Human:
    def __init__(self,name):
        print("Human object create")
        self.name =name
        self.head = self.Head()

    def info(self):
        print("Hello, My Name Is: ",self.name)
        print("I am full busy with: ")
        self.head.talk()
        self.head.brain.think()

    class Head:
        def __init__(self):
            print("Head object created")
            self.brain = self.Brain()
        def talk(self):
            print("talking...")

        class Brain:
            def __init__(self):
                print("Brain object created")
            def think(self):
                print("thinking...")

h = Human("Shrikrushna")
h.info()