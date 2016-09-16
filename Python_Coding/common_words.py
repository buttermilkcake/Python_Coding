def count_word(filename):
    """Count the number of times the word 'the' appears in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    
    else:
        # Count approximate number of times 'the appears in the file."
        words = contents.split()
        print(words)
        print("The word 'the occures: " + str(words.count("the")))
        
filenames = ['the_golden_bat.txt', 'the_potato_child.txt']
for filename in filenames:
    count_word(filename)
            
