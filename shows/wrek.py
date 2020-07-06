from urllib.parse import urlsplit, urlparse
import urllib
import urllib.request
import os, time
# import datetime
from shows_dict import shows
from download import download

def main():
    for show in shows:
        show_name = str(show)
        url = shows[show]
        # year = current_year()
        week = str("Week " + current_week())
        save_path = "C:/Users/Owner/Projects/wrek-project/shows/show_data"
        complete_path = os.path.join(save_path, show_name, week)

        with urllib.request.urlopen(url) as response:
            html = response.read()
            html = html.decode("utf-8")
            # split the M3U (playlist) into seperate URLs
            split_urls = html.split('\n')
            print(split_urls)
            # isolate the mp3 name and use it as the file save name
            for urls in split_urls:
                if urls == '':
                    pass
                else:
                    sep_urls = urlparse(urls)
                    mp3_filename = os.path.basename(sep_urls[2])
                    download(urls, mp3_filename, complete_path)


if __name__ == '__main__':
    main()
