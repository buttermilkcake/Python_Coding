prompt = "\nWhy do you like programming?"
prompt += "\nEnter 'quit' when you're done. "

filename = 'programming_poll.txt'

while True:
    response = input(prompt)

    if response == 'quit':
        break
    else:
        print("I like programming because " + response + ".\n")
        with open(filename, 'a') as f:
            f.write(response + "\n")
