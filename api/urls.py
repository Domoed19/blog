from django.urls import include, path
from rest_framework import routers
from api.posts.views import PostViewSet
from api.cars.views import CarViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'cars', CarViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include("rest_framework.urls", namespace="rest_framework")),
]
