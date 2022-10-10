from __future__ import unicode_literals
import youtube_dl
print("Insert the link")
link = input ("")

#youtube-dl --external-downloader ffmpeg --external-downloader-args "-ss 00:01:00.00 -to 00:02:00.00"

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320'
    }],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])