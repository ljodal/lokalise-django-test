from django.urls import path

from .views import my_view, template_view

urlpatterns = [
    path("", my_view, name="index"),
    path("test", template_view, name="test"),
]
