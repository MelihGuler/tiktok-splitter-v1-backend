
from urllib.parse import urlparse
from marshmallow import Schema, fields, ValidationError, validates
from api.constants.url import TIKTOK_HOST_NAME
from  marshmallow.validate import Range

class VideoSchema(Schema):
    video_url = fields.URL(required=True, schemes=['https'])
    part_length = fields.Integer(required=False, strict=True, validate=[Range(min=1, error="Part length must be greater than 0")])
    
    @validates('video_url')
    def validate_video_url(self, value):
        if urlparse(value).netloc != TIKTOK_HOST_NAME:
            raise ValidationError('Invalid Domain Name')
