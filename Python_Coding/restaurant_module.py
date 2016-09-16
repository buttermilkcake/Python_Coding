"""A class that can be used to represent a restaurant."""

class Restaurant():
    """A simple attempt to describe a restaurant."""

    def __init__(self, name, cuisine):
        """Initialize attributes to describe a restaurant."""
        self.name = name
        self.cuisine = cuisine

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = self.name + ", " + self.cuisine
        return long_name.title()

    def open(self):
        """Announce that the restuarant is open."""
        print(self.name.title() + " is now open!")
