# config.py
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://porquin:churrasco@localhost:3306/gasto_dev'


class ProductionConfig(Config):
    ENV = "gastoion"
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://porquin:churrasco@gasto-db:3306/gasto'
