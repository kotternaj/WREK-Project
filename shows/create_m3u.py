import os

def create_m3u(urls, filepath):
    save_path = "C:/Users/Owner/Projects/wrek-project/shows/show_data/"
    current_path = os.path.join(save_path, filepath)
    os.chdir(current_path)
    print(urls)
    with open("playlist.txt", "a") as f:
        for url in urls: f.write(url + '\n')

    filename = 'playlist.txt'
    base = os.path.splitext(filename)[0]
    os.rename(filename, base + '.m3u')
    cur_dir = os.getcwd()
    filename = os.path.join(cur_dir, 'playlist.m3u')
    print(filepath)
    return(current_path, filename)
if __name__ == '__main__':
    test = ['https://storage.googleapis.com/wrek-01/Goldsoundz/28/Tue1800.mp3',
               'https://storage.googleapis.com/wrek-01/Goldsoundz/28/Tue1830.mp3']
    path = 'Goldsoundz/28'
    create_m3u(test, path)
