from django.urls import path, include
from .views import *



urlpatterns = [
    path(route='', view = country_data, name = "country_data"),
    path(route='country_features/', view = country_features, name = "country_features"),
    path(route='gdp-per-cap/', view =display_gdp_graph, name="display_gdp_graph"),
    path(route='population-evolution/', view =display_population_evolution_graph, name="display_population_evolution_graph"),
    path(route='population-2023-details/', view =display_2023_population_graph, name="display_2023_population_graph"),
    path(route='search_country', view =search_country, name="search_country"),
]
