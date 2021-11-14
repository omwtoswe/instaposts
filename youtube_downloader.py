#installation 
#pip3 install pytube

from pytube import YouTube

# link of the video to be downloaded
yt = YouTube('https://www.youtube.com/watch?v=ZVwwoK7d3Yo')
yt.streams.filter(progressive=True, file_extension='mp4').order_by(
    'resolution')[-1].download()
