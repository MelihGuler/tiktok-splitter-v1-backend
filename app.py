from flask import Flask
from api.route.video import video_api

def create_app():
    app = Flask(__name__)

     ## Initialize Config
    app.config.from_pyfile('config.py')
    app.register_blueprint(video_api, url_prefix='/api/video')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host=app.config['FLASK_RUN_HOST'], port=app.config['FLASK_RUN_PORT'])
