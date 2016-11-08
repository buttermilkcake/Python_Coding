favorite_numbers = {'carmen': ['5', '7', '9'],
                    'lucy': ['2', '4', '6'],
                    'george': ['0', '1', '3'],
                    'macy': ['3', '4', '5'],
                    'lana': ['8', '9', '6']
                    }

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + "'s favorite numbers are:")
    for number in numbers:
        print("\t" + number)
