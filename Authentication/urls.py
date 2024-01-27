from django.urls import path, include
from .views import login_view

urlpatterns = [
    path(route='', view = include('Main_App.urls')),
    path(route='', view=login_view, name="login_view"),
]
