prompt = "\nPlease enter a topping you would like on your pizza:"
prompt += "\n(Enter 'quit' when you are finished.)"

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print("I will add " + message + " to your pizza.")
