class Privileges():
    """List the privileges that an admin user has."""

    def __init__(self, privileges):
        """Initialize the attributes of privileges."""
        self.privileges = privileges['can delete post', 'can ban user',
                                 'can rule the world']

    def show_privileges(self):
        """Print a statement showing the privileges of an admin user."""
        print("An admin user can do the following: " + self.privileges + ".")

my_user = Privileges
print(my_user.show_privileges)
