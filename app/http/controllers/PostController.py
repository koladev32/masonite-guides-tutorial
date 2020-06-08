"""A PostController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller

from app.Post import Post

class PostController(Controller):
    """PostController Controller Class."""

    def __init__(self, request: Request):
        """PostController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        return Post.all()
