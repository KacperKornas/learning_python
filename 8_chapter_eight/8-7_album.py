def make_album(name, title, tracks =''):
    """Return a dictionary  of information about music."""
    if tracks:
        album = {
            'Artist': name.title() ,
            'Title': title.title(),
            'Number': tracks
        }
    else:
        album = {
            'Artist': name.title(),
            'Title': title.title()
        }
    return album

music = make_album('kaleo', 'broken bones')
print(music)

music_1 = make_album('mon mcLean', 'american pie',2)
print(music_1)

music_2 = make_album('the silent comedy', 'barholomew',4)
print(music_2)



