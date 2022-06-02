from moviepy.editor import *
import time
from tkinter import filedialog as fd
import tkinter as tk
from tkinter import font
from moviepy.editor import AudioFileClip
import os

print("select video file")
filename = fd.askopenfilename()

fontDir = "C:\Program Files\ImageMagick-7.1.0-Q16-HDRI"

#bad loops
while True:
  try:
    starttime = int(input("Enter start time (in seconds): "))
    break
  except ValueError:
    print("Please input integer only...")
    continue

while True:
  try:
    endtime = int(input("Enter end time (in seconds): "))
    break
  except ValueError:
    print("Please input integer only...")
    continue

print("selct audio file")
music = fd.askopenfilename()
audio = AudioFileClip(music)

#GUI
window = tk.Tk()
window.title("Test")
window.configure(width = 900, height = 500)
window.configure()

testDisplay = tk.Label()
testDisplay.pack()

fonts = list(font.families())
fonts.sort()

defaultValue = tk.StringVar()
defaultValue.set(fonts[5])

def close():
  window.destroy()

label1 = tk.Label(text = "Select Font")
label1.pack()

dropDown = tk.OptionMenu(window, defaultValue, *fonts)
dropDown.pack()

getButton1 = tk.Button(text = "close", command = close)
getButton1.pack()

window.mainloop()

theFont = defaultValue.get()
theFont = theFont.replace(" ", "-")
print(theFont)

outputFile = input("Name the output file: ")
textText = input("Add The title text: ")

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
ffmpeg_extract_subclip((filename), (starttime), (endtime), targetname="cut.mp4")

#setting export files
videoclip = VideoFileClip("cut.mp4")
new_clip = videoclip.without_audio()
new_clip.write_videofile("noaud_cut.mp4")

#gets duration of audio file
auddur = int(audio.duration)

#text setup and rendering text image
txt = TextClip(txt = textText, color="white", bg_color="black", fontsize = 30, font = theFont)
txt = txt.set_pos('center').set_duration(auddur)

#math for number of times to loop video
clip = VideoFileClip("noaud_cut.mp4")
numTimes = auddur/clip.duration

#Resizing
clip_resized = clip.resize((400, 200))

#Code that does! work for looping
loopedClip = clip_resized.loop(n=numTimes)

# Set the audio of the clip
loopedClip = loopedClip.set_audio(audio)

#put text on top of video
loopedClip = CompositeVideoClip([loopedClip, txt])

# Export the clip
loopedClip.write_videofile(outputFile + ".mp4", fps=10)

#delete temp files
os.remove("cut.mp4")
os.remove("noaud_cut.mp4")
