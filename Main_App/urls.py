from django.urls import path, include
from .views import *



urlpatterns = [
    path(route='economy/', view = include('Economics_App.urls')),
    path(route='', view = index, name = "index"),
    path(route='about/', view = about_us, name = "about_us"),
    path(route='contact_us/', view = contact_us, name = "contact_us"),
]
