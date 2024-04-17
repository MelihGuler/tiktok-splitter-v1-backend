
from urllib.parse import urlparse
from flask import Flask, Response, request, jsonify
from marshmallow import Schema, fields, ValidationError, EXCLUDE, validates
import tiktok


class BaseSchema(Schema):
    video_url = fields.URL(required=True, schemes=['https'])
    
    @validates('video_url')
    def validate_video_url(self, value):
        if urlparse(value).netloc != 'www.tiktok.com':
            raise ValidationError('Invalid Domain Name')
        
    
tiktok.specify_browser('firefox')

app = Flask(__name__)

@app.route("/download/video/tiktok", methods = ['POST'])
def download_tiktok_video():
    schema = BaseSchema(unknown=EXCLUDE)
    
    try:
        # Validate request body against schema data types
        request_body = schema.load(request.json)
    except ValidationError as err:
        print(err.messages.get('video_url'))
        # Return a nice message if validation fails
        return jsonify({'error': err.messages}), 400
    
    video = tiktok.save_tiktok(request_body['video_url'], 'firefox')

    if video is None:
        return Response('An error during fetch the video', 500)
    
    else:
        final_response = Response(video, 200, mimetype='video/mp4',
                      content_type='video/mp4', direct_passthrough=True)
        return final_response
        



if __name__ == '__main__':
    app.run(threaded=True)
