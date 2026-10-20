from moviepy.editor import ColorClip, TextClip, CompositeVideoClip

# Video size
WIDTH = 800
HEIGHT = 450

# Video duration
DURATION = 5

# Background
background = ColorClip(
    size=(WIDTH, HEIGHT),
    color=(20, 50, 100),
    duration=DURATION
)

# Text
text = TextClip(
    text="akshay rai new Video",
   # text ="bca new and first python program"
    font_size=60,
    color="white"
)
text = text.with_position("center")

# Background aur text ko combine karo
video = CompositeVideoClip([background, text])

# MP4 file create karoS
video.write_videofile(
    "my_video.mp4",
    fps=24,
    codec="libx264"
)

print("Akshay Rai! 🎬")