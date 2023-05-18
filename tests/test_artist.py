from lib.artist import *

"""
Artist constructs test
"""
def test_artist_constructs():
    artist = Artist(1, "Pixies", "Rock")
    assert artist.id == 1
    assert artist.name == "Pixies"
    assert artist.genre == "Rock"

"""
Test if artists are the same
"""
def test_artists_are_the_same():
    artist1 = Artist(1, "artist1", "genre1")
    artist2 = Artist(1, "artist1", "genre1")
    assert artist1 == artist2

"""
Test the format as string
"""
def test_format_string():
    artist = Artist(1, "artist1", "genre1")
    assert str(artist) == "artist1"