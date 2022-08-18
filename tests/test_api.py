
import pytest

from django.test.client import Client
from tests.factories import PostFactory
from tests.factories import CarFactory
from posts.models import Post


@pytest.mark.django_db
class TestViews:

    def setup_method(self):
        self.client = Client()

    def test_posts_list(self):
        PostFactory.create_batch(5)
        response = self.client.get("/api/posts/")
        assert response.status_code == 200
        assert len(response.data) == 5


    def test_post_create(self):
        data={"title":"title", "text":"text"}
        response = self.client.post("/api/posts/", data=data)

        assert response.status_code == 201
        response = self.client.get("/api/posts/")
        assert response.status_code == 200
        assert len(response.data) == 1


@pytest.mark.django_db
class TestViews:

    def setup_method(self):
        self.client = Client()

    def test_posts_list(self):
        CarFactory.create_batch(5)
        response = self.client.get("/api/cars/")
        assert response.status_code == 200
        assert len(response.data) == 5


    def test_post_create(self):
        data={"title":"title", "model":"model", "color":"color", "text":"text"}
        response = self.client.post("/api/cars/", data=data)

        assert response.status_code == 201
        response = self.client.get("/api/cars/")
        assert response.status_code == 200
        assert len(response.data) == 1