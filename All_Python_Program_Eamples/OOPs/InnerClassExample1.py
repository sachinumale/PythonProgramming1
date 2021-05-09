class Human:
    class Head:
        def talk(self):
            print("Talking...")

        class Brain:
            def think(self):
                print("Thinking...")

human = Human()
head = human.Head()
head.talk()
brain = head.Brain()
brain.think()
