from django.http import HttpResponseRedirect
from django.shortcuts import render
from multiprocessing import Process
from .models import *

def double_processes():
    create_countries = Process(target=Country.clear_data_and_import)
    create_countries.start()
    create_regions = Process(target=Region.clear_data_and_import)
    create_regions.start()
    create_countries.join()
    create_regions.join()
    

def country_data(request):
    """View for displaying all countries and regions in the database using multiprocessing

    Args:
        request (HttpRequest): Handled by django

    Returns:
        HttpResponse: returns the html template with countries and region lists
    """
    
    # double_processes()   #Uncomment these line in case wanting to reimport data from csv files
    regions = Region.objects.all()
    countries = Country.objects.all()
    return render(request=request, template_name= 'countries.html', context= {"countries": countries, "regions": regions})


def search_country(request):
    """View for searching for a country/region

    Args:
        request (HttpRequest): Handled by django

    Returns:
        HttpResponse: returns the list of countries containing the search value
    """
    
    if request.method == 'POST':
        countries = []
        regions = []
        name = request.POST.get('name')
        try:
            countries = Country.objects.filter(name__icontains=name)
            regions = Region.objects.filter(name__icontains=name)     
        except ValueError:
            print(f"Invalid value: {name}")
            return HttpResponseRedirect(redirect_to=country_data)
        # checking values where found
        if len(countries) + len(regions) == 0 :
            return HttpResponseRedirect(redirect_to=country_data)
        else:
            return render(request=request, template_name="search_country.html", context={"countries": countries, "regions": regions})
    
    # no post form
    else:
        return HttpResponseRedirect(redirect_to=country_data)
    

def country_features(request):
    """View for displaying the documentation for the app and the available features

    Args:
        request (HttpRequest): Handled by django

    Returns:
        HttpResponse: returns the html template with countries list
    """
    
    return render(request=request, template_name="country_features.html", context={})


def display_gdp_graph(request):
    """View for displaying gdp evolution graph for each country

    Args:
        request (HttpRequest): Handled by django

    Returns:
        HttpResponse: returns the html template with the country to display 
    """
    
    if request.method == 'POST':
        id = request.POST.get("id")
        if request.POST.get("Test") == "Country": # test to know if we're looking for a country or region
            print(1)
            try:
                country = Country.objects.get(id= int(id))
                return render(request=request, template_name="display_gdp_country_graph.html", context={"country": country})
            except ObjectDoesNotExist:
                print(f"Object not found with id: {id}")
                return HttpResponseRedirect(redirect_to=country_data)
            
        elif request.POST.get("Test") == "Region":
            try:
                region = Region.objects.get(id= int(id))
                return render(request=request, template_name="display_gdp_region_graph.html", context={"region": region})
            except ObjectDoesNotExist:
                print(f"Object not found with id: {id}")
                return HttpResponseRedirect(redirect_to=country_data)
    else:
        return HttpResponseRedirect(redirect_to=country_data)


def display_population_evolution_graph(request):
    """View for displaying population evolution graph

    Args:
        request (HttpRequest): Handled by django

    Returns:
        HttpResponse: returns the html template with the country to display
    """
    
    if request.method == 'POST':
        id = request.POST.get("id")
        try:
            country = Country.objects.get(id= int(id))
            return render(request=request, template_name="display_population_evolution_graph.html", context={"country": country})
        except ObjectDoesNotExist:
            print(f"Object not found with id: {id}")
            return HttpResponseRedirect(redirect_to=country_data)
    else:
        return HttpResponseRedirect(redirect_to=country_data)


def display_2023_population_graph(request):
    """View for displaying 2023 country data ()

    Args:
        request (HttpRequest): Handled by django

    Returns:
        HttpResponse: returns the html template with the country to display
    """
    
    if request.method == 'POST':
        id = request.POST.get("id")
        try:
            country = Country.objects.get(id= int(id))
            return render(request=request, template_name="display_2023_population_graph.html", context={"country": country})
        except ObjectDoesNotExist:
            print(f"Object not found with id: {id}")
            return HttpResponseRedirect(redirect_to=country_data)
    else:
        return HttpResponseRedirect(redirect_to=country_data)    

