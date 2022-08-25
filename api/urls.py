from django.urls import include, path
from rest_framework import routers

from api.auth.views import RegisterView, LoginView
from api.posts.views import PostViewSet
from api.cars.views import CarViewSet
from api.purchases.views import PurchaseList, ProductList, ProductAdd

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'cars', CarViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('purchases/', PurchaseList.as_view(), name="purchases"),
    path('products/', ProductList.as_view(), name="products"),
    path('productadd/', ProductAdd.as_view(), name="product-add"),
    path('auth/', include("rest_framework.urls", namespace="rest_framework")),
]
