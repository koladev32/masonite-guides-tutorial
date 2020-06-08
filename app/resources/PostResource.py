from masonite.api.resources import Resource
from app.Post import Post
from masonite.api.serializers import JSONSerializer

class UserResource(Resource, JSONSerializer):
    model = Post