from django.urls import include, path
from rest_framework import routers

from api.auth.views import RegisterView, LoginView
from api.posts.views import PostViewSet
from api.cars.views import CarViewSet
from api.purchases.views import PurchaseListViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'cars', CarViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('purchase/', PurchaseListViewSet.as_view(), name="purchase"),
    path('auth/', include("rest_framework.urls", namespace="rest_framework")),
]
