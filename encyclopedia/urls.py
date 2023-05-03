from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("new", views.new, name="new"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("save/<str:title>", views.save, name="save"),
    path("delete/<str:title>", views.delete, name="delete"),
    path("random", views.random, name="random"),
    path("<str:title>/", views.error, name="error")
]

