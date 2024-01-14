from django.urls import path, include
from .views import *



urlpatterns = [
    path(route='countries/', view = include('Countries_App.urls')),
    path(route='', view = index, name = "index"),
    path(route='about/', view = about_us, name = "about_us"),
    path(route='contact_us/', view = contact_us, name = "contact_us"),
]
