import os

def create_m3u(urls, filepath):
    save_path = "C:/Users/Owner/Projects/wrek-project/shows/show_data/"
    current_path = os.path.join(save_path, filepath)
    os.chdir(current_path)
    with open("playlist.txt", "a") as f: # create a playlist with every MP3 URL used in a show
        for url in urls: f.write(url + '\n')

    filename = 'playlist.txt'
    base = os.path.splitext(filename)[0]
    os.rename(filename, base + '.m3u') # rename from .txt to .m3u
    filename = os.path.join(current_path, 'playlist.m3u')
    head_tail = os.path.split(filename) # split the URL in two
    file = head_tail[1] # specify playlist.m3u as the file
    current_path = os.path.normpath(current_path)
    temp_path = current_path.split(os.sep)
    del temp_path[0:7] # results in /<showname>/<week>/playlist.m3u
    upload_path = os.path.join(*temp_path).replace("\\","/")
    return(upload_path, file)
