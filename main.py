from pytube import YouTube
import re


def is_valid_http_url(url):
    if not re.match(r'^https?://', url):
        return False

    if not re.match(r'^[a-zA-Z0-9-._~/?#:=&%+]+$', url):
        return False
    return True


def downloader(url):
    yt_vid = YouTube(url)
    resolutions = yt_vid.streams.filter(progressive=True).order_by('resolution').desc()

    video_1080p = resolutions.filter(res='1080p').first()
    video_720p = resolutions.filter(res='720p').first()

    if video_1080p:
        video = video_1080p
        print('Downloading 1080p resolution...')
    elif video_720p:
        video = video_720p
        print('Downloading 720p resolution...')
    else:
        print('No 1080p and 720p resolutions found for download.')
        return

    try:
        print('Video downloading started...')
        video.download()
        print('Video downloaded successfully!')
    except Exception as e:
        print(e)


url = input('Enter video url: ')
while is_valid_http_url(url) is False:
    url = input('Enter valid url: ')

if is_valid_http_url(url):
    downloader(url)
