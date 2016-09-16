age = input("What is your age? ")
age = int(age)

if age <= 3:
    print("\nYour ticket price is free.")
elif age >= 12:
    print("\nYour ticket price is $15.")
else:
    print("\nYour ticket price is $10.")                
    
