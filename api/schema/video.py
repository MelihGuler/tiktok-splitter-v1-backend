
from urllib.parse import urlparse
from marshmallow import Schema, fields, ValidationError, validates
from api.constants.url import TIKTOK_HOST_NAME

class VideoSchema(Schema):
    video_url = fields.URL(required=True, schemes=['https'])
    
    @validates('video_url')
    def validate_video_url(self, value):
        if urlparse(value).netloc != TIKTOK_HOST_NAME:
            raise ValidationError('Invalid Domain Name')
