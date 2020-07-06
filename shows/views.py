from django.shortcuts import render
from .shows_dict import shows as sh
from .current_week import current_week

def home(request):
    shows = sh
    context = {'shows': shows}
    print(shows)
    return render(request, 'shows/home.html', context)

def mode_7(request):
    # week = str("Week " + current_week())
    weeks = [i for i in (range(20, current_week() + 1))]
    # weeks = str(weeks)
    context = {'weeks': weeks }
    return render(request, 'shows/mode_7.html', context)
