import json

favorite = input("What is your favorite number? ")

filename = 'favorite.json'
with open(filename, 'a') as f_obj:
    json.dump(favorite, f_obj)
   
