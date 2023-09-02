def make_album(name, title,):
    """Return a dictionary  of information about music."""

    album = {
            'Artist': name.title() ,
            'Title': title.title(),
        }

    return album

while True:
    print('\nPlease tell me your favorite artist: ')
    print("(enter 'q' at any time to quit)")

    name = input('Artist: ')
    if name == 'q':
        break

    print('\nPlease tell me their best song: ')
    print("(enter 'q' at any time to quit")

    title = input('Title: ')
    if title == 'q':
        break

    album = make_album(name, title)
    print(album)