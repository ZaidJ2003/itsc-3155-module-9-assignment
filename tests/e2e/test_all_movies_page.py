# TODO: Feature 1
import pytest
from app import app
from src.repositories.movie_repository import get_movie_repository

def test_all_movies():
    test_client = app.test_client()
    response = test_client.post('/movies', data={
        'title': 'Spiderman',
        'director': 'Zaid Jebril',
        'rating': 5
    }, follow_redirects=True)

    # data = response.data.decode('utf-8')

    assert response.status_code == 200
    assert b'<td>Spiderman</td' in response.data
    assert b'<td>Zaid Jebril</td' in response.data
    assert b'<td>5</td' in response.data