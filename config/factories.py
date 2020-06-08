from orator.orm import Factory
from app.User import User

from app.Post import Post

factory = Factory()


def users_factory(faker):
    return {
        'name': faker.name(),
        'email': faker.email(),
        'password': '$2b$12$WMgb5Re1NqUr.uSRfQmPQeeGWudk/8/aNbVMpD1dR.Et83vfL8WAu',  # == 'secret'
    }

def posts_factory(faker):
    return{
        'author': faker.name(),
        'title': faker.name(),
        'description': faker.paragraph()
    }

factory.register(User, users_factory)
factory.register(Post, posts_factory)
