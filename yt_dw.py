from pytube import YouTube
link = input("Enter the link:")
yt=YouTube(link)
yd=yt.streams.get_highest_resolution()
yd.download("D:\yt download")