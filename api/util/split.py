
from moviepy.editor import VideoFileClip
from io import BytesIO

def split_video(video, part_length):
    full_duration = VideoFileClip(BytesIO(video)).duration
    start_pos = 0

    parts = []

    while start_pos < full_duration:
        end_pos = start_pos + part_length
        if end_pos > full_duration:
            end_pos = full_duration

        clip = VideoFileClip(BytesIO(video)).subclip(start_pos, end_pos)
        start_pos = end_pos
        parts.append(clip)

    return parts
