from .views import addPost
from django.conf.urls import url
urlpatterns = [
    url("^addPost/$", addPost)
]