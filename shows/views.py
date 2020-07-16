from django.shortcuts import render
from .shows_dict import shows
from .current_week import current_week
from .upload import upload_to_gcs
from .get_show_url import get_m3u_link

def home(request):
    context = {'shows': shows}
    print(shows)
    return render(request, 'shows/home.html', context)

def mode7(request):
    playlist_links = get_m3u_link('mode7')
    context = {'playlist_links': playlist_links}
    return render(request, 'shows/mode7.html', context)

def goldsoundz(request):
    playlist_links = get_m3u_link('goldsoundz')
    context = {'playlist_links': playlist_links}
    return render(request, 'shows/goldsoundz.html', context)
