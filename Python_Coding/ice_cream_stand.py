class Restaurant():
    """A class that describes names and cuisines of restaurants."""

    def __init__(self, name, kind):
        """Initialize restaurant name and cuisine attributes."""
        self.name = name
        self.kind = kind

    def get_descriptive_name(self):
        long_name = self.name + ' ' + self.kind
        return long_name.title()

my_restaurant = Restaurant('story', 'bistro')

print("The restaurant's name is " + my_restaurant.name.title() + 
      ", and it is a " + my_restaurant.kind + ".")
my_restaurant.get_descriptive_name()
          
class IceCreamStand(Restaurant):
    """A simple attempt to showcase flavors for an ice cream stand."""

    def __init__(self, name, kind):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an ice cream stand.
        """
        super().__init__(name, kind)
        self.flavors_1 = 'vanilla'
        self.flavors_2 = 'white chocolate'
        self.flavors_3 = 'pb panic'
    
    def describe_flavors(self):
        """Print a statement describing the flavors."""
        print("The flavors at Sticky Sweet are " + self.flavors_1 + ", " + self.flavors_2 + ", and " +
              self.flavors_3 + ".")

my_flavors = IceCreamStand('sticky sweet', 'ice cream stand')

print("The restaurant's name is " + my_flavors.name.title() +
      ", and it is a " + my_flavors.kind + ".")
print(my_flavors.get_descriptive_name())
my_flavors.describe_flavors()
