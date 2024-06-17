from moviepy.editor import ImageSequenceClip, VideoFileClip, AudioFileClip

# List of image file paths
image_files = [
    "1.png",
    "2.png",
    "3.png",
    "4.png",
    "5.png",
    "6.png",
    "7.png",
    "8.png",
    "9.png",
    "10.png"
]

# Extend the image sequence to match the desired video duration
desired_duration = 10  # seconds
image_duration = 2  # seconds per image
total_images_needed = desired_duration // image_duration
extended_image_files = image_files * (total_images_needed // len(image_files) + 1)

# Create the image sequence clip
clip = ImageSequenceClip(extended_image_files, fps=1/image_duration)

# Write the image sequence to a video file
output_video = "dragon_video.mp4"
clip.write_videofile(output_video, codec='libx264')

# Load the created video file
video = VideoFileClip("dragon_video.mp4")

# Load audio file
audio = AudioFileClip("dragons-music.mp3")

# Trim audio to match video duration
video_duration = video.duration
audio = audio.subclip(0, video_duration)

# Set the audio of the video to the trimmed audio clip
video = video.set_audio(audio)

# Write the output video with the new audio
output_video_final = "output_video.mp4"
video.write_videofile(output_video_final, codec="libx264", audio_codec="aac")
