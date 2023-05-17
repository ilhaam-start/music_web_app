# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)

POST /albums
  title: string
  release_year: integer
  artist_id: integer
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python

# POST /submit
#  Parameters:
#    name: Leo
#    message: Hello world
#  Expected response (200 OK):
"""
Thanks Leo, you sent this message: "Hello world"
"""

# POST /submit
#  Parameters: none
#  Expected response (400 Bad Request):
"""
Please provide a name and a message
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
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
def test_post_album(web_client):
    response = web_client.post('/albums', data={'title': 'title1', 'release_year': '2023', 'artist_id': '1'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == None

"""
When we make a GET request to /albums
Then we should get Expected response 200 OK and we get the output of all records in our database
"""
def test_get_albums(web_client):
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == [
      "Album(1, Doolittle, 1989, 1)"
      "Album(2, 'Surfer Rosa', 1988, 1)"
    ]

"""
When we make a GET request to /albums/1
Then we should get Expected response 200 OK and we get the output the first item
"""
def test_get_album_1(web_client):
    response = web_client.get('/albums/1')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album(1, Doolittle, 1989, 1)"


```


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
