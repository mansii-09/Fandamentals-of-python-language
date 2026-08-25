def extract_artist(song_title):
    dash_index = song_title.index("-")
    artist = song_title[dash_index + 1:]
    return artist.strip()

song = "perfect - Ed sheeran"
print(extract_artist(song))