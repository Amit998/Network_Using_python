import pytube


url='https://www.youtube.com/playlist?list=PL7yh-TELLS1G9mmnBN3ZSY8hYgJ5kBOg-'



playlist=pytube.Playlist(url)


# print(playlist)
for url in playlist:
    video=pytube.YouTube(url)
    stream=video.streams.get_by_itag(22)
    stream.download()