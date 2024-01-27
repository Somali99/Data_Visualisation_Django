from django.urls import path
from .views import *



urlpatterns = [
    path(route='', view = country_data, name = "country_data"),
    path(route='country_features/', view = country_features, name = "country_features"),
    path(route='gdp/gdp-per-cap', view =display_gdp_graph, name="display_gdp_graph"),
    path(route='pop/population-evolution', view =display_population_evolution_graph, name="display_population_evolution_graph"),
    path(route='demography/population-2023-details', view =display_2023_population_graph, name="display_2023_population_graph"),
    path(route='search_country', view =search_country, name="search_country"),
    path(route='gdp/', view = gdp_only, name="gdp_only"),
    path(route='pop/', view = pop_only, name="pop_only"),
    path(route='demography/', view = demography, name="demography"),
]
