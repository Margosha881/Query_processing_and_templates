import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


with open(BUS_STATION_CSV, newline='',encoding='utf-8') as f:
    reader = csv.DictReader(f)
    stations = []
    for rows in reader:
        stations.append({'Name': rows['Name'], 'Street': rows['Street'], 'District': rows['District']})


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get('page',1))
    pagination = Paginator(stations,10)
    page = pagination.get_page(page_number)
    data = page.object_list

    context = {
        'bus_stations': data,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
