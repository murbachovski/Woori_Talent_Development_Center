from moviepy import VideoFileClip, TextClip, CompositeVideoClip

# Load file example.mp4 and keep only the subclip from 00:00:10 to 00:00:20
# Reduce the audio volume to 80% of its original volume

clip = (
    VideoFileClip("_data/vehicles.mp4")
    .subclipped(5, 20)
    .with_volume_scaled(0.8)
)

# Generate a text clip. You can customize the font, color, etc.
txt_clip = TextClip(
    font="v1_data_aug/Ant.ttf",
    text="ABCDEFG",
    font_size=150,
    color='blue'
).with_duration(5).with_position('center')

# Overlay the text clip on the first video clip
final_video = CompositeVideoClip([clip, txt_clip])
final_video.write_videofile("result.mp4")