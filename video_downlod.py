import yt_dlp
url = input("Enter url of the video to download :")
ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
print("video has been downloaded successfully")


