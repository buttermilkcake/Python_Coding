class Restaurant():
    """A class that describes names and cuisines of restaurants."""

    def __init__(self, name, cuisine):
        """Initialize restaurant name and cuisine attributes."""
        self.name = name
        self.cuisine = cuisine

    def describe(self):
        """Describe each restaurant listed."""
        print(self.name.title() + " serves " + self.cuisine.title() + ".")

    def open(self):
        """Announce that the restuarant is open."""
        print(self.name.title() + " is now open!")

my_restaurant = Restaurant('story', 'european')
his_restaurant = Restaurant('novel', 'organic')
her_restaurant = Restaurant('coalvines', 'american')

print("The restaurant's name is " + my_restaurant.name.title() + ".")
print("The cuisine is " + my_restaurant.cuisine.title() + ".")
my_restaurant.describe()
                     
print("The restaurant's name is " + his_restaurant.name.title() + ".")
print("The cuisine is " + his_restaurant.cuisine.title() + ".")
his_restaurant.describe()

print("The restaurant's name is " + her_restaurant.name.title() + ".")
print("The cuisine is " + her_restaurant.cuisine.title() + ".")
her_restaurant.describe()              
