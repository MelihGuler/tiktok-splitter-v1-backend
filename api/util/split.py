
import tempfile
import os
from moviepy.editor import VideoFileClip
from flask import Response

def split_video(video, part_length):
    # Create a temporary file to write full video into it.
    temp_file = tempfile.NamedTemporaryFile(mode='w+b', suffix='.mp4', delete=False)
    temp_file.write(video)
    # Go to the top of the file then, close the file.
    temp_file.seek(0)
    temp_file.close()
    
    # Create VideoClip object from saved video file.
    video_clip = VideoFileClip(temp_file.name)
    full_duration = video_clip.duration
    
    parts = []
    start_pos = 0
    # Split video into parts according to part_length parameter
    while start_pos < full_duration:
        end_pos = start_pos + part_length
        # If end_position exceeds the video length, set end_position to the end of the video.
        if end_pos > full_duration:
            end_pos = full_duration

        # Create video part from start_pos to end_pos
        clip = VideoFileClip(temp_file.name).subclip(start_pos, end_pos)
        # Move start_position forward
        start_pos = end_pos
       
        # Give a temporary name to video part. 
        clip_filename = f'{temp_file.name[:-4]}-part{len(parts)+1}.mp4'
        
        # Save video part with clip_filename and close
        clip.write_videofile(clip_filename)
        clip.close()
        video_clip.close()

        # Add video part name to the [parts] array
        parts.append(clip_filename)
        
    
    # Delete full video file as we dont need it anymore
    os.remove(os.path.join(temp_file.name))
    
    return parts