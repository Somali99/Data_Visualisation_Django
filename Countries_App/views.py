from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *

def country_data(request):
    print(Country.clear_data_and_import())   #Uncomment this line in case wanting to reimport data from csv 
    countries = Country.objects.all()
    return render(request=request, template_name= 'countries.html', context= {"countries": countries})

def search_country(request):
    if request.method == 'POST':
        name = request.POST.get("search")
        try:
            country = Country.objects.get(name__icontains=name)
            return render(request= request, template_name= "search_country.html", context= {"country": country})
        except ObjectDoesNotExist:
            print(f"Object not found with name: {name}")
            return HttpResponseRedirect(redirect_to=country_data)
    else:
        return HttpResponseRedirect(redirect_to=country_data)

def country_features(request):
    # displays and documents the various features of the economy app
    return render(request= request, template_name= "country_features.html", context={})

def display_gdp_graph(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        try:
            country = Country.objects.get(id= int(id))
            print(country)
            return render(request=request, template_name= "display_country_graph.html", context= {"country": country})
        except ObjectDoesNotExist:
            print(f"Object not found with id: {id}")
            return HttpResponseRedirect(redirect_to=country_data)
    else:
        return HttpResponseRedirect(redirect_to=country_data)

def display_population_evolution_graph(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        try:
            country = Country.objects.get(id= int(id))
            print(country)
            return render(request=request, template_name= "display_population_evolution_graph.html", context= {"country": country})
        except ObjectDoesNotExist:
            print(f"Object not found with id: {id}")
            return HttpResponseRedirect(redirect_to=country_data)
    else:
        return HttpResponseRedirect(redirect_to=country_data)

def display_2023_population_graph(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        try:
            country = Country.objects.get(id= int(id))
            print(country)
            render(request=request, template_name= "display_2023_population_graph.html", context= {"country": country})
        except ObjectDoesNotExist:
            print(f"Object not found with id: {id}")
            return HttpResponseRedirect(redirect_to=country_data)
    else:
        return HttpResponseRedirect(redirect_to=country_data)    

