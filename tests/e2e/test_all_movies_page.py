# TODO: Feature 1
from app import app

#check to see no table if no saved movies
def test_no_movies():
    test_client = app.test_client()
    response = test_client.post('/movies', data={}, follow_redirects=True)
    
    assert b'<h1 class="text-center">No Saved Movies!</h1>'

def test_one_movie():
    test_client = app.test_client()
    response = test_client.post('/movies', data={
        'title': 'Spiderman',
        'director': 'Zaid Jebril',
        'rating': 3
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'<td>Spiderman</td>' in response.data
    assert b'<td>Zaid Jebril</td>' in response.data
    assert b'<td>3</td>' in response.data


#Testing that page loads and all movies are loaded
def test_all_movies():
    test_client = app.test_client()
    
    response = [
    {
        'title': 'Spiderman',
        'director': 'Zaid Jebril',
        'rating': 5
    },
    {
        'title': 'Batman',
        'director': 'Sam Smith',
        'rating': 3
    }
    ]

    response = test_client.post('/movies', data={'movies': response}, follow_redirects=True)

    assert response.status_code == 200

    assert b'<td>Spiderman</td>' in response.data
    assert b'<td>Batman</td>' in response.data

