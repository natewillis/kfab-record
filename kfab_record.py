#!/usr/bin/python3

from urllib.request import urlopen
from datetime import datetime

if __name__ == '__main__':

    # Inputs
    stream_url = 'https://c3icy.prod.playlists.ihrhls.com/1325_icy'
    max_file_size = 1048576 * 5
    buffer_size = max_file_size/2

    while True:

        # Outputs
        file_size = 0
        storage_path = "/media/wddisk1/media/radio/kfab/" + 'audio-' + datetime.strftime(datetime.now(), "%Y%m%d%H%M%S") + '.aac'

        with open(storage_path, 'wb') as file:
            stream = urlopen(stream_url)

            while file_size <= max_file_size:
                file.write(stream.read(buffer_size))
                file_size += buffer_size
