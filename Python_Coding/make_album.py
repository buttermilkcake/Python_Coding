def get_make_album(artist_name, album_title):
    """Return a dictionary of information about an album."""
    album = artist_name + ' ' + album_title
    return album

while True:
    print("\nPlease tell me an artist's name and album title:")
    print("(enter 'q' at any time to quit)")

    a_name = input("Artist name: ")
    if a_name == 'q':
        break

    a_title = input("Album title: ")
    if a_title == 'q':
        break

    make_album = get_make_album(a_name, a_title)
    print("\n " + make_album)
