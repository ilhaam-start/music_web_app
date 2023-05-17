# Tests for your routes go here

"""
When we make a POST request to /albums
And we put no paramaters
Then we should get Expected response 400 Bad Request - "Invalid - You need to add an album"
"""
def test_invalid_post(web_client):
    response = web_client.post('/albums')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'Invalid - You need to add an album'


"""
When we make a POST request to /albums
And we put title, release_year, artist_id as the body parameters
Then we should get Expected response 200 OK - no content but details added
"""
def test_post_album(db_connection, web_client):
    db_connection.seed("seeds/albums_table.sql")
    response = web_client.post('/albums', data={'title': 'title1', 'release_year': '2023', 'artist_id': '1'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ''

"""
When we make a GET request to /albums
Then we should get Expected response 200 OK and we get the output of all records in our database
"""
def test_get_albums(web_client):
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album(1, Doolittle, 1989, 1), Album(2, Surfer Rosa, 1988, 1), Album(3, title1, 2023, 1)"
    

"""
When we make a GET request to /albums/1
Then we should get Expected response 200 OK and we get the output the first item
"""
def test_get_album_1(web_client):
    response = web_client.get('/albums/1')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album(1, Doolittle, 1989, 1)"



# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===
