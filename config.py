
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    FLASK_RUN_HOST = '0.0.0.0'
    FLASK_RUN_PORT = 8080
    