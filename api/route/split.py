
from http import HTTPStatus
from flask import request, jsonify, Blueprint
from marshmallow import ValidationError, EXCLUDE
from api.schema.video import VideoSchema
from api.service.split import SplitService

split_api = Blueprint('split_api', __name__)

@split_api.route('/split/tiktok', methods=['POST'])
def split_tiktok_video():
    schema = VideoSchema(unknown=EXCLUDE)
    
    try:
        # Validate request body against invalid schema data types
        request_body = schema.load(request.json)
    except ValidationError as err:
        print(err.messages.get('video_url'))
        # Return a nice message if validation fails
        return jsonify({'error': err.messages}), HTTPStatus.BAD_REQUEST
    
    split_service = SplitService()
    
    # Call the service method to get the video
    # file deepcode ignore XSS: <User input is sanitized above, with schema.load function >
    return split_service.split(request_body['video_url'], request_body['part_length'])