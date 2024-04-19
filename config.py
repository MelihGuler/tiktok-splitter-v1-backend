"""[General Configuration Params]
"""
FLASK_RUN_HOST = 'localhost'
FLASK_RUN_PORT = 8080

from os import path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))
