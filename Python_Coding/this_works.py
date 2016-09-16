class People():
    """"A simple attempt to represent some information."""

    def __init__(self, name, salary):
        """Initialize people attributes."""
        self.name = name
        self.salary = salary
        self.new_raise = 0
        self.new_salary = 0
        
    def get_descriptive_info(self):
        """Return a neatly formatted bundle of info."""
        long_stuff = self.name + ' ' + str(self.salary)
        return long_stuff.title()

    def give_raise(self):
        """Print a statement showing the person's salary increase."""
        print("This person is getting an increase of " + str(self.new_raise) +
              ".")

    def increment_raise(self, monies):
        """Show the new_raise amount."""
        self.new_raise += monies

    def new_salary(self):
        """Set the salary to the new amount."""
        print("This person's new salary is " + str(new_raise + self.salary)
                                                   + ".")

my_rich_people = People('sally', 60000)
print(my_rich_people.get_descriptive_info())

my_rich_people.increment_raise(10000)
my_rich_people.give_raise()

my_rich_people.new_salary()
