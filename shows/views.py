from django.shortcuts import render
from .shows_dict import shows
from .current_week import current_week
from .upload import upload_to_gcs
from .get_show_url import list_blobs, find_show_week

def home(request):
    context = {'shows': shows}
    print(shows)
    return render(request, 'shows/home.html', context)

def mode7(request):
    # weeks = [i for i in (range(20, current_week() + 1))]
    urls, week, filename = find_show_week(shows)
    url1 = urls[0]
    filename1 = filename[0]
    url2 = urls[1]
    filename2 = filename[1]

    context = {'week': week, 'url1': url1, 'url2': url2,
               'filename1': filename1, 'filename2': filename2}
    return render(request, 'shows/mode7.html', context)

def goldsoundz(request):
    weeks = [i for i in (range(20, current_week() + 1))]
    context = {'weeks': weeks }
    return render(request, 'shows/goldsoundz.html', context)
