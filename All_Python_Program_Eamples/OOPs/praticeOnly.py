class Movie:
    def __init__(self,name,hero,heroien):
        self.name = name
        self.hero = hero
        self.herioes = heroien

    def title(self):
        print("Name of Movie:", self.name)
        print("Hero Name:", self.hero)
        print("Heroien Name:", self.herioes)
list_movies = []
while True:
    name = input("Enter Name of Movie: ")
    hero = input("Enter Hero Name: ")
    herioen = input("Enter Heroien Name: ")

    o = Movie(name,hero,herioen)
    list_movies.append(o)
    print('Movie Added to the list successfully...')
    option = input('Do you want to add one more movie [Yes|No]:').lower()
    while option not in ('yes', 'y', 'no', 'n'):
        option = input('Choose Valid Option[Yes|No]:').lower()
    if option in ('no', 'n'):
        break


for movie in list_movies:
    movie.title()
    print()