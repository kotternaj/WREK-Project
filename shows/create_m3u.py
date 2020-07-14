import os

def create_m3u(urls, filepath):
    save_path = "C:/Users/Owner/Projects/wrek-project/shows/show_data/"
    print("Save path is: ", save_path)
    current_path = os.path.join(save_path, filepath)
    print("Current path is now: ", current_path)
    os.chdir(current_path)
    print("We changed dir into the cwd, which is: ", os.getcwd())
    print("Creating M3U file...")
    with open("playlist.txt", "a") as f:
        for url in urls: f.write(url + '\n')

    filename = 'playlist.txt'
    base = os.path.splitext(filename)[0]
    os.rename(filename, base + '.m3u')
    filename = os.path.join(current_path, 'playlist.m3u')
    head_tail = os.path.split(filename)
    file = head_tail[1]
    current_path = os.path.normpath(current_path)
    print(current_path)
    temp_path = current_path.split(os.sep)

    del temp_path[0:7] #/<showname>/<week>/<mp3>
    upload_path = os.path.join(*temp_path).replace("\\","/")
    print(upload_path)
    print(file)
    return(upload_path, file)
