from django.urls import path
from . import views


urlpatterns = [
    path("landlord/", views.landlord_signup, name="landlord"),
    path("regular/", views.regular_signup, name="regular"),
    path("", views.index, name="index")
]