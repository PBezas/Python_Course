# Chicken Coop Exercise
# Suppose we have a big ol chicken coop in our backyard full of very productive hens. We're going to model our chickens with python! We want to keep track of how many eggs each individual Chicken lays, and at the same time we want to track the total number of eggs all hens have laid.

#  Create a Chicken  class.  Each Chicken has a species  and a name , as well as an integer attribute called eggs . eggs should always start out at 0.

# Each Chicken should also have an instance method called lay_egg() which should increment and then return that particular Chicken's eggs  attribute. lay_egg()  should also increment a class variable called total_eggs

# c1 = Chicken(name="Alice", species="Partridge Silkie")
# c2 = Chicken(name="Amelia", species="Speckled Sussex")
# Chicken.total_eggs #0
# c1.lay_egg()  #1
# Chicken.total_eggs #1
# c2.lay_egg()  #1
# c2.lay_egg()  #2
# Chicken.total_eggs #3


class Chicken:
    total_eggs = 0

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self._eggs = 0

    def lay_egg(self):
        self._eggs += 1
        Chicken.total_eggs += 1

    def get_eggs_num(self):
        return f"This chicken has layed: {self._eggs} eggs"


chic1 = Chicken(name="Alice", species="Partridge Silkie")
chic2 = Chicken(name="Amelia", species="Speckled Sussex")

chic1.lay_egg()
print(chic1.get_eggs_num())
print(f"total_coop_eggs: {Chicken.total_eggs} eggs")

chic2.lay_egg()
print(chic2.get_eggs_num())
print(f"total_coop_eggs: {Chicken.total_eggs} eggs")

chic1.lay_egg()
print(chic1.get_eggs_num())
print(f"total_coop_eggs: {Chicken.total_eggs} eggs")

chic1.lay_egg()
print(chic1.get_eggs_num())
print(f"total_coop_eggs: {Chicken.total_eggs} eggs")

chic2.lay_egg()
print(chic2.get_eggs_num())
print(f"total_coop_eggs: {Chicken.total_eggs} eggs")
