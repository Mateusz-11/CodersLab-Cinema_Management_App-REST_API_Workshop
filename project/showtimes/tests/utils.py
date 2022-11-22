from random import sample
from movielist.models import Movie
from faker import Faker
from showtimes.models import Screening
import pytz
faker = Faker("pl_PL")
TZ = pytz.timezone(TIME_ZONE)

def random_movies():
    """Return 3 random Movies from db."""
    movies = list(Movie.objects.all())
    return sample(movies, 3)



