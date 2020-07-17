from urllib.parse import urlsplit, urlparse
import urllib
import urllib.request
import os, time
from upload import upload_to_gcs
from shows_dict import shows
from download import download
from current_week import current_week
from get_show_url import find_show_url
from create_m3u import create_m3u

def main():
    for show in shows:
        show_name = str(show)
        url = shows[show]
        week = str(current_week()-2)
        save_path = "C:/Users/Owner/Projects/wrek-project/shows/show_data"
        complete_path = os.path.join(save_path, show_name, week)

        with urllib.request.urlopen(url) as response:
            html = response.read()
            html = html.decode("utf-8")
            split_urls = html.split('\n') # split the M3U (playlist) into seperate URLs
            for urls in split_urls:
                if urls == '':
                    pass
                else:
                    sep_urls = urlparse(urls) # isolate the mp3 name and
                    mp3_filename = os.path.basename(sep_urls[2]) # use it as the file save name
                    upload_file_path, mp3_filename = download(urls, mp3_filename, complete_path) #download each mp3
                    upload_to_gcs(upload_file_path, mp3_filename) # upload each mp3 to GCS
        show_urls, filepath = find_show_url(show_name) # create a list of mp3 URLs for show that just downloaded
        local_path, m3u_file = create_m3u(show_urls, filepath) # create a playlist
        upload_to_gcs(local_path, m3u_file) # upload that playlist to GCS

if __name__ == '__main__':
    main()
