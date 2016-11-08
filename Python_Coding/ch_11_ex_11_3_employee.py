class People():
    """"A simple attempt to represent some information."""

    def __init__(self, name, salary):
        """Initialize people attributes."""
        self.name = name
        self.salary = salary
        self.new_raise = 0
        
    def get_descriptive_info(self):
        """Return a neatly formatted bundle of info."""
        long_stuff = self.name + ' ' + str(self.salary)
        return long_stuff.title()

    def give_raise(self):
        """Print a statement showing the person's salary increase."""
        print("This person is getting an increase of " + str(self.new_raise) +
              " and their new salary is " + str(self.new_raise + self.salary) +
              ".")

    def update_raise(self, money):
        """Set the salary to the given amount."""
        self.new_raise = money

    def increment_raise(self, monies):
        """Add the raise amount to the new_raise amount."""
        self.new_raise += monies

my_rich_people = People('sally', 60000)
print(my_rich_people.get_descriptive_info())

my_rich_people.increment_raise(5000)    
my_rich_people.give_raise()
