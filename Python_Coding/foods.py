my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli']
friend_foods = ['pizza', 'falafel', 'carrot cake', 'ice cream']

print("Here are the first three foods on my list:")
for my_food in my_foods[:3]:
    print(my_food)

print("\nMy friend's first three foods are:")
for friend_food in friend_foods[:3]:
    print(friend_food)

print("My list of foods are:")
for my_food in my_foods[0:4]:
    print(my_food)

print("\nMy friend's list of foods are:")
for friend_food in friend_foods[0:4]:
    print(friend_food)
