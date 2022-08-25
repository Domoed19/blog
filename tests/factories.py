import factory
from django.contrib.auth.models import User

from factory.django import DjangoModelFactory
import factory.fuzzy
from posts.models import Post
from cars.models import Car
from shop.models import Product, Purchase, COLOR_CHOICES


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

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("word")
    email = factory.Faker("email")


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Faker("company")
    # slug = factory.fuzzy.FuzzyChoice(dict(COLOR_CHOICES).keys())
    cost = factory.Faker("pyint", min_value=50, max_value=150)


class PurchaseFactory(DjangoModelFactory):
    class Meta:
        model = Purchase

    user = factory.SubFactory(UserFactory)
    product = factory.SubFactory(ProductFactory)
    count = factory.Faker("pyint", min_value=1, max_value=5)