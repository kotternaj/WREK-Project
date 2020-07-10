from django.shortcuts import render
from .shows_dict import shows
from .current_week import current_week
from .upload import upload_to_gcs
from .get_show_url import list_blobs, find_show_url

def home(request):
    context = {'shows': shows}
    print(shows)
    return render(request, 'shows/home.html', context)

def mode7(request):
    url_dict, filename = find_show_url('Mode7')
    mp3_list = filename[0], filename[1]
    # print(url_dict)
    # for x in url_dict[0]:
    #     print(x)
    # weeks = [i for i in (range(20, current_week() + 1))]
    # urls, weeks, mp3s = find_show_url('Mode7')
    # url1, url2 = urls
    # mp3_00, mp3_30 = filename
    # url2 = urls[1]
    # filename2 = filename[1]
    # print(mp3_list)
    context = {'url_dict': url_dict, 'mp3_list': mp3_list }
    # context = {'url_dict': url_dict, 'mp3_00': mp3_00, 'mp3_30': mp3_30 }
    # context = {'weeks': weeks, 'urls': urls, 'mp3s': mp3s}
    return render(request, 'shows/mode7.html', context)

def goldsoundz(request):
    weeks = [i for i in (range(20, current_week() + 1))]
    context = {'weeks': weeks }
    return render(request, 'shows/goldsoundz.html', context)
