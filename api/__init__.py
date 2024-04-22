
from flask import Flask
from api.route.video import video_api
from api.route.split import split_api
from api.constants.url import URL_PREFIX
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)

     ## Initialize Config
    app.config.from_object(config_class)
    
    #Register blueprints
    app.register_blueprint(video_api, url_prefix=URL_PREFIX)
    app.register_blueprint(split_api, url_prefix=URL_PREFIX)

    return app
