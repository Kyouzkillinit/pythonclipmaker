from tkinter import filedialog as fd

filename = fd.askopenfilename()

starttime = input("enter start-time (in seconds): ")

endtime = input("enter end-time (in seconds): ")

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
ffmpeg_extract_subclip((filename), 14, 27, targetname="cut.mp4")
