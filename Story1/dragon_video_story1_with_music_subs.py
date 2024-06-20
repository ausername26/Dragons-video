import os
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.config import change_settings

# Function to generate text clip for subtitles
def subtitle_generator(txt):
    return TextClip(txt, font='Arial', fontsize=24, color='white')

# Path to your video file
video_path = "dragon_video_story1_with_music.mp4"

# Load the video clip
video = VideoFileClip(video_path)

# Define subtitles
subs = [   (("00:00:00", "00:00:04"), "In a hidden valley, where mist curled around ancient trees and flowers bloomed in vibrant hues"),
    (("00:00:05", "00:00:10"), "there lived a small dragon named Ember. Unlike the tales told by elders, Ember wasn't fearsome or mighty"),
    (("00:00:11", "00:00:15"), "instead, she loved to chase fireflies at dusk and play among the shimmering pools that dotted the valley."),
    (("00:00:16", "00:00:22"), "One day, a lost traveler stumbled upon Ember's valley, expecting danger but finding only serenity"),
    (("00:00:23", "00:00:24"), "Ember approached with curiosity, her scales glinting softly in the sunlight. The traveler, amazed by the dragon's gentle nature, realized that not all legends hold true."),
    (("00:00:25", "00:00:26"), "They shared a meal of berries and stories under the shade of an old oak tree."),
    (("00:00:27", "00:00:28"), "the traveler continued on their journey"),
    (("00:00:29", "00:00:32"), "forever changed by their encounter with a dragon who showed them the beauty of peace and harmony."),
    ]

# Create the subtitles clip
subtitles = SubtitlesClip(subs, subtitle_generator)

# Composite video with subtitles
video_with_subs = CompositeVideoClip([video, subtitles.set_pos(('center', 'bottom'))])

# Write the result to a file
video_with_subs.write_videofile("output_video_with_subs.mp4", codec='libx264')
