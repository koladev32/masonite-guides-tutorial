"""Post Model."""

from config.database import Model


class Post(Model):
    """Post Model."""
    __table__ = 'posts'
    __fillable__ = ['author','title','description']
