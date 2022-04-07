from moviepy.editor import *
import time
from tkinter import filedialog as fd
from moviepy.editor import AudioFileClip

print("select video file")
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

print("selct audio file")
music = fd.askopenfilename()
audio = AudioFileClip(music)

outputFile = input("Name the output file")

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
ffmpeg_extract_subclip((filename), (starttime), (endtime), targetname="cut.mp4")

videoclip = VideoFileClip("cut.mp4")
new_clip = videoclip.without_audio()
new_clip.write_videofile("noaud_cut.mp4")

auddur = int(audio.duration)
print(type(auddur))
#time.sleep(5000)

clip = VideoFileClip("noaud_cut.mp4")
numTimes = auddur/clip.duration

print(str(auddur))

#Resizing
clip_resized = clip.resize((400, 200))

#Code that does work for looping
loopedClip = clip_resized.loop(n=numTimes)

# Set the audio of the clip
loopedClip = loopedClip.set_audio(audio)

# Export the clip
loopedClip.write_videofile(outputFile + ".mp4", fps=10)
