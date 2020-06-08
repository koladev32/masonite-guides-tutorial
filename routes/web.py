"""Web Routes."""

from masonite.routes import Get, Post
from app.resources.PostResource import PostResource

ROUTES = [
    Get('/', 'WelcomeController@show').name('welcome'),
    Get('/posts','PostController@show').name('posts'),

    #Api 
    PostResource('/api/posts').routes(),
]
