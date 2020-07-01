from urllib.parse import urlsplit, urlparse
import urllib
import urllib.request
import os, time
import datetime
from datetime import date
from shows import shows
from upload import upload_to_gcs

def main():
    for show in shows:
        show_name = str(show)
        url = shows[show]
        year = current_year()
        week = str("Week " + current_week())
        save_path = "C:/Users/Owner/Projects/wrek-project/shows/show_data"
        complete_path = os.path.join(save_path, year, show_name, week)

        with urllib.request.urlopen(url) as response:
            html = response.read()
            html = html.decode("utf-8")
            # split the M3U (playlist) into seperate URLs
            split_urls = html.split('\n')
            print(split_urls)
            # isolate the mp3 name and use it as the save name
            for urls in split_urls:
                if urls == '':
                    pass
                else:
                    sep_urls = urlparse(urls)
                    mp3_filename = os.path.basename(sep_urls[2])
                    download(urls, mp3_filename, complete_path)
                    upload_to_gcs(mp3_filename)

def download(urls, mp3_filename, complete_path):
    if os.path.exists(complete_path):
        print('Directory "%s" already exists' %complete_path)
    else:
        os.makedirs(complete_path)
        print('New directory "%s" was created' %complete_path)
    os.chdir(complete_path)
    try:
        print('Saving file: ', mp3_filename)
        urllib.request.urlretrieve(urls, mp3_filename)
        print('Successfully saved: ', mp3_filename)

    except(ValueError):
        pass

# determine current week to be used to name the auto-generated dirs
def current_week():
    y, m, d = date.today().year, date.today().month, date.today().day
    week_num = datetime.date(y, m, d).isocalendar()[1]
    week = str(week_num)
    return week

def current_year():
    year_ = str(date.today().year)
    return year_

if __name__ == '__main__':
    main()
