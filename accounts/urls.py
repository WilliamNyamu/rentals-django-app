from django.urls import path
from . import views


urlpatterns = [
    path("landlord/", views.landlord, name="landlord"),
    path("regular/", views.regular, name="regular"),
    path("", views.index, name="index")
]