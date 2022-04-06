from tkinter import filedialog as fd
from moviepy.editor import VideoFileClip

filename = fd.askopenfilename()

while True:
  try:
    starttime = int(input("Enter start-time (in seconds): "))
    break
  except ValueError:
      print("Please input integer only...")  
      continue

while True:
  try:
    endtime = int(input("Enter end-time (in seconds): "))
    break
  except ValueError:
      print("Please input integer only...")  
      continue

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
ffmpeg_extract_subclip((filename), (starttime), (endtime), targetname="cut.mp4")

videoclip = VideoFileClip("cut.mp4")
new_clip = videoclip.without_audio()
new_clip.write_videofile("noaud_cut.mp4")

