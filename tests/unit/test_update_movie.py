# TODO: Feature 5
from flask.testing import FlaskClient
import pytest
from app import app
from src.repositories.movie_repository import get_movie_repository


@pytest.fixture(scope='module')
def test_app() -> FlaskClient:
    return app.test_client()

# test page load
def test_update_movie_page(test_app: FlaskClient) -> None:

    # create a movie
    movie_repo = get_movie_repository()
    movie_repo.create_movie('Test Movie', 'Test Director', 5)
    movie = movie_repo.get_movie_by_title('Test Movie')

    response = test_app.get(f'/movies/{movie.movie_id}/edit')
    data = response.data.decode()

    assert len(movie_repo.get_all_movies()) == 1
    assert response.status_code == 200
    assert '<h1 class="mb-5">Edit Movie</h1>' in data


