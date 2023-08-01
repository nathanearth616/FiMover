# importing the needed modules

import os
import shutil

# variabling the locations
the_thing_ein_location = 'C:\\Users\\miyamoto\\Downloads\\'
location = 'C:\\Users\\miyamoto\\Videos\\yt_videos\\'
pic_location = 'C:\\Users\\miyamoto\\Pictures\\'

#listing the items in the download folder and checking if it contains specitfic words
youtube_videos = [f for f in os.listdir(the_thing_ein_location) if '.mp4' in f.lower()]
pictures = [f for f in os.listdir(the_thing_ein_location) if '.png' in f.lower() or '.jpg' in f.lower() or '.jpeg' in f.lower()]

# for loops that moves the file that has that specific word from the download folder to where i want
for video in youtube_videos:
    where_video_from = os.path.join(the_thing_ein_location, video)
    where_video_to = os.path.join(location, video)
    shutil.move(where_video_from, where_video_to)

    print(f'{video} relocated to {where_video_to}')

for picture in pictures:
    where_pic_from = os.path.join(the_thing_ein_location, picture)
    where_pic_to = os.path.join(pic_location, picture)
    shutil.move(where_pic_from, where_pic_to)

    print(f'{picture} relocated to {where_pic_to}')

print('files moved successfully')