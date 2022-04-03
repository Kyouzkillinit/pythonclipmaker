from tkinter import filedialog as fd

filename = fd.askopenfilename()

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
# ffmpeg_extract_subclip("your_video.mp4", start_seconds, end_seconds, targetname="cut.mp4")
ffmpeg_extract_subclip((filename), 14, 27, targetname="cut.mp4")
