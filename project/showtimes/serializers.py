from showtimes.models import Cinema
from rest_framework import serializers


class CinemaSerializer(serializers.ModelSerializer):
    movies = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='movies-detail'
    )
    class Meta:
        model = Cinema
        fields = ['name', 'city', 'movies']