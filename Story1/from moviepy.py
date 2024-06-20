from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips

# File paths (adjust these paths according to your files)
video_path = 'dragon_video_story1.mp4'
music_path = 'meow-unstoppable-ai-cover.mp3'

# Load video clip
video_clip = VideoFileClip(video_path)

# Load audio clip
audio_clip = AudioFileClip(music_path)

# Set audio duration same as video duration
audio_clip = audio_clip.subclip(0, video_clip.duration)

# Add audio to video
video_clip = video_clip.set_audio(audio_clip)

# Write the video file with merged audio
output_path = 'dragon_video_story1_with_music.mp4'
video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

# Close the clips
video_clip.close()
audio_clip.close()
