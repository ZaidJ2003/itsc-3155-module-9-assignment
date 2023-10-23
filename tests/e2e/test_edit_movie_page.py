# TODO: Feature 5
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

# test post request
def test_update_movie_post(test_app: FlaskClient) -> None:

    # create a movie
    movie_repo = get_movie_repository()
    movie_repo.clear_db()
    movie_repo.create_movie('Test Movie', 'Test Director', 5)
    movie = movie_repo.get_movie_by_title('Test Movie')

    assert len(movie_repo.get_all_movies()) == 1
    assert movie is not None

    response = test_app.post(f'/movies/{movie.movie_id}', data={
        'title': 'Test Movie 2',
        'rating': '3',
        'director': 'Test Director 2'
    }, follow_redirects=True)

    movie2 = movie_repo.get_movie_by_title('Test Movie 2')
    assert response.status_code == 200
    assert movie2 is not None
    assert len(movie_repo.get_all_movies()) == 1
    assert movie_repo.get_movie_by_title('Test Movie') is None