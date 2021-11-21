import pytube
from pytube import YouTube
import pytesseract
link = input("Enter the youtube link : ")
video = YouTube(link)
print(f"Title: {video.title}\n"
      f"Description: {video.description}\n"
      f"Rating: {video.rating}\n")
stream = video.streams.get_highest_resolution()
stream.download(r"F:\Youtube_videos")
print("Download is done...")
