from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *


def country_data(request):
    """View for displaying all countries in the database

    Args:
        request (HttpRequest): 

    Returns:
        HttpResponse: returns the html template with countries list
    """
    # print(Country.clear_data_and_import())   #Uncomment this line in case wanting to reimport data from csv files
    countries = Country.objects.all()
    return render(request=request, template_name= 'countries.html', context= {"countries": countries})


def search_country(request):
    """View for searching for a country

    Args:
        request (HttpRequest): 

    Returns:
        HttpResponse: returns the list of countries containing the search value
    """
    if request.method == 'POST':
        name = request.POST.get("search")
        try:
            country = Country.objects.get(name__icontains=name)
            return render(request=request, template_name="search_country.html", context={"country": country})
        except ObjectDoesNotExist:
            print(f"Object not found with name: {name}")
            return HttpResponseRedirect(redirect_to=country_data)
    else:
        return HttpResponseRedirect(redirect_to=country_data)


def country_features(request):
    """View for displaying the documentation for the app and the available features

    Args:
        request (HttpRequest): 

    Returns:
        HttpResponse: returns the html template with countries list
    """
    return render(request=request, template_name="country_features.html", context={})


def display_gdp_graph(request):
    """View for displaying gdp evolution graph for each country

    Args:
        request (HttpRequest): 

    Returns:
        HttpResponse: returns the html template with the country to display 
    """
    if request.method == 'POST':
        id = request.POST.get("id")
        try:
            country = Country.objects.get(id= int(id))
            return render(request=request, template_name="display_gdp_graph.html", context={"country": country})
        except ObjectDoesNotExist:
            print(f"Object not found with id: {id}")
            return HttpResponseRedirect(redirect_to=country_data)
    else:
        return HttpResponseRedirect(redirect_to=country_data)


def display_population_evolution_graph(request):
    """View for displaying population evolution graph

    Args:
        request (HttpRequest): 

    Returns:
        HttpResponse: returns the html template with the country to display
    """
    if request.method == 'POST':
        id = request.POST.get("id")
        try:
            country = Country.objects.get(id= int(id))
            print(country)
            return render(request=request, template_name="display_population_evolution_graph.html", context={"country": country})
        except ObjectDoesNotExist:
            print(f"Object not found with id: {id}")
            return HttpResponseRedirect(redirect_to=country_data)
    else:
        return HttpResponseRedirect(redirect_to=country_data)


def display_2023_population_graph(request):
    """View for displaying 2023 country data ()

    Args:
        request (HttpRequest): 

    Returns:
        HttpResponse: returns the html template with the country to display
    """
    if request.method == 'POST':
        id = request.POST.get("id")
        try:
            country = Country.objects.get(id= int(id))
            print(country)
            return render(request=request, template_name="display_2023_population_graph.html", context={"country": country})
        except ObjectDoesNotExist:
            print(f"Object not found with id: {id}")
            return HttpResponseRedirect(redirect_to=country_data)
    else:
        return HttpResponseRedirect(redirect_to=country_data)    


