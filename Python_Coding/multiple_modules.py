"""A set of classes to represent admin users."""

from user import User
from admin import Admin

my_user = User('dan', 'doughty', 'diggity2')
my_admin = Admin('julie', 'stark', 'cake5')
print(my_user.get_descriptive_name())
print(my_admin.get_descriptive_name())
my_admin.privileges.show_privileges()
