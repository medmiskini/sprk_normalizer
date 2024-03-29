from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from sprk_normalizer.users.api.views import UserViewSet
from sprk_normalizer.products.urls import urlpatterns as product_urls

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls
urlpatterns += product_urls

