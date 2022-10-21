import pytest

from django.test.client import Client

from shop.models import Purchase
from tests.factories import UserFactory, PurchaseFactory, ProductFactory


@pytest.mark.django_db
class TestPurchasesViews:
    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()

    def test_product_list(self):
        ProductFactory(cost=30)
        response = self.client.get("/api/products/?min_cost=50")
        assert response.status_code == 200
        assert response.data["count"] == 0

        ProductFactory(cost=70)
        response = self.client.get("/api/products/?min_cost=50")
        assert response.status_code == 200
        assert response.data["count"] == 1

    def test_purchases_list(self):
        purchase_1 = PurchaseFactory()
        self.client.force_login(purchase_1.user)
        response = self.client.get("/api/purchases/")

        assert response.status_code == 200
        assert response.data["count"] == 1
        assert (
            response.data["results"][0]["product"]["title"] == purchase_1.product.title
        )

        purchase_2 = PurchaseFactory(user=self.user)
        self.client.force_login(self.user)
        response = self.client.get("/api/purchases/")

        assert response.status_code == 200
        assert response.data["count"] == 1
        assert (
            response.data["results"][0]["product"]["title"] == purchase_2.product.title
        )

        assert Purchase.objects.count() == 2

    def test_product_create(self):
        product = ProductFactory
        self.client.force_login(self.user)

        data = {"title": "title", "color": "color", "cost": "cost"}
        response = self.client.post("/api/productadd/", data=data)
        assert response.status_code == 201

        response = self.client.get("/api/productadd/")
        assert response.status_code == 200
        assert len(response.data["results"]) == 1
