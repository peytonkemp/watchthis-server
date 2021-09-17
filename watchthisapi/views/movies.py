from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from watchthisapi.models import Movie


class MovieView(ViewSet):

    def retrieve(self, request, pk=None):
        """Handle GET requests for single movie
        Returns:
            Response -- JSON serialized game instance
        """
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
            """Handle GET requests to movies resource
            Returns:
                Response -- JSON serialized list of movies
            """
            movies = Movie.objects.all()
            # Support filtering movies by game
            # game = self.request.query_params.get('game_id', None)
            # if game is not None:
            #     movies = movies.filter(game__id=game)

            # for movie in movies:
            #     movie.joined = gamer in movie.attendees.all()

            serializer = MovieSerializer(
                movies, many=True, context={'request': request})
            return Response(serializer.data)

class MovieSerializer(serializers.ModelSerializer):
    """JSON serializer for movies"""

    class Meta:
        model = Movie
        fields = ('id', 'title', 'backdrop_path',
                  'overview', 'popularity', 'poster_path', 'release_date', 'revenue',
                  'runtime', 'tagline', 'vote_average')
        depth = 1












