import os
import sys
import pytest

from faker import Faker
from rest_framework.test import APIClient


sys.path.append(os.path.dirname(__file__))
faker = Faker("pl_PL")


@pytest.fixture
def client():
    client = APIClient()
    return client