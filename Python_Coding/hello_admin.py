current_users = ['lucy', 'sasha', 'jade', 'rory', 'tara']

new_users = ['Rory', 'Tara', 'poppy', 'carmen', 'khaleesi']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Sorry, you will have to pick a new user name.")

    else:
        print("The username is available.")

ordinal_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for ordinal_number in ordinal_numbers:
    if ordinal_number == '1':
        print("1st")
    if ordinal_number == '2':
        print("2nd")
    elif ordinal_number == '3':
        print("3rd")
    else:
        print(ordinal_number + "th")
