import os

def create_m3u(url1, url2):
    urls = (url1, url2)
    print(urls)
    with open("playlist.txt", "a") as f:
        for url in urls: f.write(url + '\n')

    filename = 'playlist.txt'
    base = os.path.splitext(filename)[0]
    os.rename(filename, base + '.m3u')

if __name__ == '__main__':
    create_m3u('https://storage.googleapis.com/wrek-01/Goldsoundz/Week28/Tue1800.mp3',
               'https://storage.googleapis.com/wrek-01/Goldsoundz/Week28/Tue1830.mp3')
