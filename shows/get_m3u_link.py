import os
from .split_url import split_url
from .get_show_url import list_blobs

def get_m3u_link(showname): # an M3U file is a playlist consistng of URLs pointing to MP3s
    m3u_dict = {}
    bucket_contents = list_blobs('wrek-01') # grab every URL in bucket
    for url in bucket_contents:
        filepath, week, file = split_url(url)
        if file == 'playlist.m3u': # if the URL ends in .m3u
            if filepath[0] == showname: # and show name in list == showname in URL
                m3u_dict.update({ week: url }) # append dict with week of year and URL to the playlist
    return(m3u_dict.items())
