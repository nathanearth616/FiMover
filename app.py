import os
import shutil

video_location = 'C:\\Users\\miyamoto\\Downloads\\'
location = 'C:\\Users\\miyamoto\\Videos\\yt_videos\\'

videos = [f for f in os.listdir(video_location) if '.mp4' in f.lower()]


for video in videos:
    where_from = os.path.join(video_location, video)
    where_to = os.path.join(location, video)
    shutil.move(where_from, where_to)

print('files moved successfullu')