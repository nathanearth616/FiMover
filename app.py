# importing the needed modules

import os
import shutil

# variabling the locations
file_location = 'C:\\Users\\miyamoto\\Downloads\\'
yt_location = 'C:\\Users\\miyamoto\\Videos\\yt_videos\\'
cs_location = 'C:\\Users\\miyamoto\\Videos\\Programming\\'
pic_location = 'C:\\Users\\miyamoto\\Pictures\\'

#checking if movies are still being torrented
# question = input("Are all files done downloading? ").lower()

# if question == 'yes':

# listing the items in the download folder and checking if it contains specitfic words
cs_videos = [f for f in os.listdir(file_location) if 'python' in f.lower()
             or 'coding' in f.lower() or 'linux' in f.lower()]

youtube_videos = [f for f in os.listdir(file_location) if '.mp4' in f.lower()]

pictures = [f for f in os.listdir(file_location) if '.png' in f.lower()
            or '.jpg' in f.lower() or '.jpeg' in f.lower()]

# movies = [f for f in os.listdir(file_location) if 'so1' in f.lower()
#             or '720p' in f.lower() or 'bluray' in f.lower() or 'complete' in f.lower()]

# for loops that moves the file that has that specific word from the download folder to where i want
for item in cs_videos:
    where_video_from = os.path.join(file_location, item)
    where_video_to = os.path.join(cs_location, item)
    shutil.move(where_video_from, where_video_to)

    print(f'{item} relocated to {where_video_to}')

for video in youtube_videos:
    where_video_from = os.path.join(file_location, video)
    where_video_to = os.path.join(yt_location, video)
    shutil.move(where_video_from, where_video_to)

    print(f'{video} relocated to {where_video_to}')

for picture in pictures:
    where_pic_from = os.path.join(file_location, picture)
    where_pic_to = os.path.join(pic_location, picture)
    shutil.move(where_pic_from, where_pic_to)

    print(f'{picture} relocated to {where_pic_to}')

print('files moved successfully')

# else:
#     print('Wait for all the movies, sia.')
