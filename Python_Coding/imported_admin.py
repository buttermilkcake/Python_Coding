"""A set of classes used to represent users."""

class User():
    """A class that describes users."""

    def __init__(self, first_name, last_name, login):
        """Initalize name, color, hair attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
                
    def get_descriptive_name(self):
       """Return a neatly formatted descriptive name."""
       long_name = (self.first_name.title() + ' ' + self.last_name.title() + ' '
       + self.login)
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
    """A class that describes admin users."""

    def __init__(self, first_name, last_name, login):
        """
        Initialize attributes of the parent class.
        Then initialize an attribute specific to Admin user.
        """
        
        super().__init__(first_name, last_name, login)
        self.privileges = Privileges()


