from flask import Flask
from api.route.video import video_api
from api.route.split import split_api
from api.constants.url import URL_PREFIX

def create_app():
    app = Flask(__name__)

     ## Initialize Config
    app.config.from_pyfile('config.py')
    
    #Register blueprints
    app.register_blueprint(video_api, url_prefix=URL_PREFIX)
    app.register_blueprint(split_api, url_prefix=URL_PREFIX)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host=app.config['FLASK_RUN_HOST'], port=app.config['FLASK_RUN_PORT'])
