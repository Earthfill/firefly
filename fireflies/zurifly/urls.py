from django.urls import include, path
from .views import index

urlpatterns = [
    path("home/", index, name="index")
]