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

def add_screenings(cinema):
    """Add 3 screenings for given cinema."""
    movies = random_movies()
    for movie in movies:
        Screening.objects.create(cinema=cinema, movie=movie, date=faker.date_time(tzinfo=TZ))


def fake_cinema_data():
    """Generate fake data for cinema."""
    return {
        "name": faker.name(),
        "city": faker.city(),
    }

def create_fake_cinema():
    pass

