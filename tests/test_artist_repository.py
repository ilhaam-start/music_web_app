from lib.artist_repository import *
from lib.artist import *

"""
Test #all method
Get a list of Artist objects
"""
def test_get_all(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repo = ArtistRepository(db_connection)
    artists = repo.all()
    assert artists == [
        Artist(1, "Pixies", "Rock"), 
        Artist(2, "ABBA", "Pop"), 
        Artist(3, "Taylor Swift", "Pop"), 
        Artist(4, "Nina Simone", "Pop")
        ]

"""
Test #find method
Get back single artist
"""
def test_find_single_artist(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repo = ArtistRepository(db_connection)
    artist = repo.find(3)
    assert artist == Artist(3, "Taylor Swift", "Pop")

"""
Test #create method
Add new artist to our list
"""
def test_create_new_artist(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repo = ArtistRepository(db_connection)
    repo.create(Artist(None, "NewArtist", "NewGenre"))
    result = repo.find(5)
    assert result == Artist(5, "NewArtist", "NewGenre")

"""
Test #delete method
remove artist from our list
"""
def test_delete_artist(db_connection):
    db_connection.seed("seeds/albums_table.sql")
    repo = ArtistRepository(db_connection)
    repo.delete(1)
    result = repo.all()
    assert result == [
        Artist(2, "ABBA", "Pop"), 
        Artist(3, "Taylor Swift", "Pop"), 
        Artist(4, "Nina Simone", "Pop")
        ]