import faker
import pytest

from django.test.client import Client
from tests.factories import PostFactory, UserFactory
from tests.factories import CarFactory
from posts.models import Post


@pytest.mark.django_db
class TestViews:

    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()
        self.fake = faker.Faker()

    def test_register(self):

        self.client.force_login(self.user)

        data={
            "email": self.fake.email(),
            "password": self.fake.md5(),
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),

        }
        response = self.client.post("/api/register/", data=data)
        assert response.status_code == 201

        response = self.client.post("/api/login/", data=data)
        assert response.status_code == 200
        assert "token" in response.data

    def test_posts_list(self):
        self.client.force_login(self.user)

        PostFactory.create_batch(15)
        response = self.client.get("/api/posts/")

        assert response.status_code == 200
        assert len(response.data["results"]) == 10
        assert response.data["count"] == 15


    def test_post_create(self):

        self.client.force_login(self.user)

        data={"title":"title", "text":"text"}
        response = self.client.post("/api/posts/", data=data)
        assert response.status_code == 201

        response = self.client.get("/api/posts/")
        assert response.status_code == 200
        assert len(response.data["results"]) == 1
        assert "image" in response.data["results"][0]


    def test_car_list(self):
        CarFactory.create_batch(5)
        response = self.client.get("/api/cars/")
        assert response.status_code == 200
        assert len(response.data["results"]) == 5


    def test_car_create(self):
        data={"title":"title", "model":"model", "color":"color", "text":"text"}
        response = self.client.post("/api/cars/", data=data)
        assert response.status_code == 201

        response = self.client.get("/api/cars/")
        assert response.status_code == 200
        assert len(response.data["results"]) == 1



