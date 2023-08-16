from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from store.views import rest

router = routers.DefaultRouter()


# store API Endpoints
router.register("brands", rest.BrandViewSet, "brands")


urlpatterns = [
    # API views
    path("rest/", include(router.urls)),
]
