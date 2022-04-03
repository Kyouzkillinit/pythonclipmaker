from moviepy.editor import VideoFileClip

videoclip = VideoFileClip("cut.mp4")
new_clip = videoclip.without_audio()
new_clip.write_videofile("noaud_cut.mp4")
