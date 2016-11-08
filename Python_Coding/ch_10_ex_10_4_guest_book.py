prompt = "\nWhat is your name?"
prompt += "\nEnter 'quit' when you're done. "

filename = 'guest_book.txt'

while True:
    name = input(prompt)

    if name == 'quit':
        break
    else:
        print("Hello " + name + "!\n")
    with open(filename, 'a') as f:
        f.write(name + "\n")
