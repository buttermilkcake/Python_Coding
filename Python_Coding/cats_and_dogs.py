filename = 'cats.txt' 

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    pass
else:
    print(contents)

filename = 'dogs.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    pass
else:
    print(contents)

filename = 'fish.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    pass
else:
    print(contents)
