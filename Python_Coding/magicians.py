def magician_names(show_magicians, make_great):
    """
    Change magician names to include the great.
    Move each name to make_great after name is altered.
    """
    while show_magicians:
        current_magician = show_magicians.pop()
        print("The Great " + current_magician.title())
        make_great.append(current_magician)

def show_make_great(make_great):
    """Print the name of each magician on the list."""
    print("\nThe following magicians have been listed:")
    for make_great in make_great:
        print(make_great.title())

show_magicians = ['mike', 'matilda', 'lilica', 'cupcake', 'bobo']
make_great = []

magician_names(show_magicians[:], make_great)
show_make_great(make_great)
print(show_magicians)
print(make_great)
print(show_magicians[:])
