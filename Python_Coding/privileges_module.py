class User():
    """A class that describers users."""

    def __init__(self, first_name, last_name, fave_color, hair_kind):
        """Initalize name, color, hair attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.fave_color = fave_color
        self.hair_kind = hair_kind
        
    def get_descriptive_name(self):
       """Return a neatly formatted descriptive name."""
       long_name = (self.first_name.title() + ' ' + self.last_name.title() + ' '
       + self.fave_color + ' ' + self.hair_kind)
       return long_name

class Privileges():
    """A simple attempt to list privileges of an admin user."""

    def __init__(self, privileges='can ban users, can delete posts, can rule the world'):
        """Initialize the privileges' attributes."""
        self.privileges = privileges

    def show_privileges(self):
        """List a set of admin user privileges."""
        print("An admin user " + self.privileges + ".")
        
class Admin(User):
    """Represents a list of priveleges specific to admins."""

    def __init__(self, first_name, last_name, fave_color, hair_kind):
        """
        Initialize attributes of the parent class.
        Then initialize an attribute specific to Admin user.
        """
        
        super().__init__(first_name, last_name, fave_color, hair_kind)
        self.privileges = Privileges()

                           
my_user = Admin('julie', 'stark', 'orange', 'curly')
print(my_user.get_descriptive_name())
my_user.privileges.show_privileges()
