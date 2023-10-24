# TODO: Feature 4
from app import get_single_movie
from src.models.movie import Movie


def test_get_single_movie():
    movie = Movie(243, 'test', 'john', 5)
    assert movie.movie_id == 243
    assert movie.director == 'john'
    assert movie.rating == 5
