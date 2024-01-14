from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(route='admin/', view=admin.site.urls),
    path(route='countries/', view = include('Countries_App.urls')),
    path(route='', view = include('Main_App.urls'))
]
