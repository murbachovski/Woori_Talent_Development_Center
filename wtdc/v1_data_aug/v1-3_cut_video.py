# from moviepy import VideoFileClip, CompositeVideoClip

# # 비디오 파일 로드 및 특정 구간 잘라내기
# clip = (
#     VideoFileClip("wtdc\_data\input.mp4").subclipped(5, 10)
# )

# # 비디오 편집
# final_video = CompositeVideoClip([clip])

# # 결과 비디오 저장
# # final_video.write_videofile("final_video.mp4")


# Import everything needed to edit video clips
from moviepy import *

# Load file example.mp4 and extract only the subclip from 00:00:10 to 00:00:20
clip = VideoFileClip("wtdc\_data\input.mp4").subclipped(10, 20)

# Generate a text clip. You can customize the font, color, etc.
txt_clip = TextClip(
    font= "wtdc\_data\kingsguard_calligraphy\KingsguardCalligraphy_PERSONAL_USE_ONLY.otf",
    text="Big Buck Bunny",
    font_size=70,
    color="white"
)

# Say that you want it to appear for 10s at the center of the screen
txt_clip = txt_clip.with_position("center").with_duration(10)

# Overlay the text clip on the first video clip
video = CompositeVideoClip([clip, txt_clip])

# Write the result to a file (many options available!)
video.write_videofile("result.mp4")
