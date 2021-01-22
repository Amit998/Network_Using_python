import pytube
from pytube.streams import Stream


url='https://www.youtube.com/watch?v=i-GvWXnVV6k'

video=pytube.YouTube(url)


stream=video.streams.get_by_itag(137)
print('Downloading..')
stream.download(filename='Shirley Setia')
print('Done')
'''
for stream in video.streams:
    if "video" in str(stream) and "mp4" in  str(stream):
        print(stream)

'''