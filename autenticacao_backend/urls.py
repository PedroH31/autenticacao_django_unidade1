from django.urls import path
from . import views

urlpatterns = [
    path("users/create/", views.create_user, name="create_user"),
    path("users/", views.get_users, name="get_users")
]