
from http import HTTPStatus
from flask import Response
import api.util.tiktok as tiktok
from api.util.split import split_video
from api.constants.errors import VIDEO_COULDNT_FETCH
from api.constants.tiktok import BROWSER_NAME

class VideoService:
    def get(self, video_url):
        video = tiktok.save_tiktok(video_url, BROWSER_NAME)

        if video is None:
            return Response(VIDEO_COULDNT_FETCH, HTTPStatus.INTERNAL_SERVER_ERROR)
    
        else:
            final_response = Response(video, HTTPStatus.OK, mimetype='video/mp4',
                      content_type='video/mp4', direct_passthrough=True)
            return final_response
    
    def split(self, video_url, part_length):
        video = tiktok.save_tiktok(video_url, BROWSER_NAME)

        if video is None:
            return Response(VIDEO_COULDNT_FETCH, HTTPStatus.INTERNAL_SERVER_ERROR)
        
        else:
            parts = split_video(video, part_length)
            return parts