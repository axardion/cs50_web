from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("create", views.create, name="create"),
    path("edit", views.edit, name="edit"),
    path("random", views.Random, name="random"),
    path("edited", views.edited, name="edited")
]
