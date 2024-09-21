import os
from dotenv import load_dotenv
from sqlalchemy import URL

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class DevelopmentConfig:
    """Development configuration."""
    ENV = os.getenv('FLASK_ENV')
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = URL.create(
        os.getenv('DB_DRIVERNAME'),
        username=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disables unnecessary overhead
    DEBUG = False
    TESTING = False
