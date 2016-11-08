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
