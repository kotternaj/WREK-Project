from django.shortcuts import render
from .shows_dict import shows as sh
# from .upload import mp3_url_dict

def home(request):
    shows = sh
    context = {'shows': shows}
    print(shows)
    return render(request, 'shows/home.html', context)
