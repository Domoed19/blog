import factory

from factory.django import DjangoModelFactory

from posts.models import Post
from cars.models import Car


class PostFactory(DjangoModelFactory):
   class Meta:
       model = Post

   title = factory.Faker("word")
   text = factory.Faker("paragraph")

class CarFactory(DjangoModelFactory):
   class Meta:
       model = Car

   title = factory.Faker("word")
   model = factory.Faker("word")
   color = factory.Faker("word")
   text = factory.Faker("paragraph")