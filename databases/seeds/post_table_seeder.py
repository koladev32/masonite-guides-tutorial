from orator.seeds import Seeder
from app.Post import Post

from config.factories import factory

class PostTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        factory(Post, 75).create()

