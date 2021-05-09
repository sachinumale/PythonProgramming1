class Movie():

    def __init__(self,title,hero,heroin):
        self.movie = title
        self.hero = hero
        self.heroin = heroin

    def info(self):
        print("Name of Movie:", self.movie)
        print("Name of Hero:", self.hero)
        print("Name of Heroin:", self.heroin)

l = []

while True:
    title = input("Enter Name of Movie: ")
    hero = input("Enter Hero Name: ")
    heroin = input("Enter Heroin Name: ")

    m = Movie(title,hero,heroin)
    l.append(m)
    option = input("Do you want to add one more data [Yes|No]: ").lower()
    while option not in ("yes","no","y","n"):
        option = input("Kindly type correct input [Yes|No]:  ").lower()

    if option in ("no","n"):
        break


print("Entered data are as followes:")
print("-"*40)

i=0
for x in l:
   print(f"No.{i+1}")
   x.info()
   print("-"*40)
   i = i + 1




