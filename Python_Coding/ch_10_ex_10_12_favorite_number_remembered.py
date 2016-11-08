import json

# Load the favorite number, if it has been stored previously.
# Otherwise, prompt for the favorite number and store it.
filename = 'favorite.json'
try:
    with open(filename) as f_obj:
        favorite = json.load(f_obj)
except FileNotFoundError:
    favorite = input("What is your favorite number? ")
    with open(filename, 'a') as f_obj:
        json.dump(favorite, f_obj)
        print("We'll remember that when you come back, " + favorite + "!")
else:
    print("I know your favorite number! It's " + favorite + "!")    
