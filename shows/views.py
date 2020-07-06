from django.shortcuts import render
from .shows_dict import shows
from .current_week import current_week
from .upload import upload_to_gcs

def home(request):
    context = {'shows': shows}
    print(shows)
    return render(request, 'shows/home.html', context)

def mode7(request):
    weeks = [i for i in (range(20, current_week() + 1))]
    context = {'weeks': weeks}
    return render(request, 'shows/mode7.html', context)

def goldsoundz(request):
    weeks = [i for i in (range(20, current_week() + 1))]
    context = {'weeks': weeks }
    return render(request, 'shows/goldsoundz.html', context)
