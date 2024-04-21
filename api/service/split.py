
import zipfile
import os
import tempfile
from http import HTTPStatus
from flask import Response

import api.util.tiktok as tiktok
from api.constants.tiktok import BROWSER_NAME
from api.constants.errors import VIDEO_COULDNT_FETCH
from api.constants.file import ZIP_FILE_NAME
from api.util.split import split_video

class SplitService:
    def split(self, video_url, part_length):
        # Get full tiktok video
        video = tiktok.save_tiktok(video_url, BROWSER_NAME)

        if video is None:
            return Response(VIDEO_COULDNT_FETCH, HTTPStatus.INTERNAL_SERVER_ERROR)
        
        else:
            # Split full video and get parts
            parts = split_video(video, part_length)
    
            # Write parts into zip file and delete parts. Then return created zip file which includes video parts.
            with tempfile.SpooledTemporaryFile() as tmp:
                with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as archive:
                    for part in parts:
                        archive.write(part, os.path.basename(part))
                        os.remove(os.path.join(part))
                
                tmp.seek(0)
                
                return Response(tmp.read(), mimetype='application/zip', headers={'Content-Disposition': f'attachment;filename={ZIP_FILE_NAME}'})
