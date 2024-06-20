import moviepy.editor as mp

# Specify the desired duration of the video in seconds
desired_duration = 38.0

# Specify durations (in seconds) for each image to appear
image_durations = [4,6,5,7,2,2,2,3]  # Example durations for each image

# Load a list of image files
image_files = ["s1.png", "s2.png", "s3.png", "s4.png", "s5.png", "s6.png", "s7.png", "s8.png"]  # Add paths to your images

# Create ImageClip instances with specified durations
images = []
for img, dur in zip(image_files, image_durations):
    image_clip = mp.ImageClip(img).set_duration(dur)
    images.append(image_clip)

# Create a sequence of images to cover the desired duration
image_sequence = mp.concatenate_videoclips(images)

# Specify the frame rate (fps) for the output video
fps = 30  # Adjust this as needed

# Write the resulting video to a file
output_path = "dragon_video_story1.mp4"
image_sequence.write_videofile(output_path, fps=fps, codec="libx264", audio_codec="aac")
