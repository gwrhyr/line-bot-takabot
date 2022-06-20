from distutils.debug import DEBUG
import os

class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{db_name}'.format(**{
        'db_name': os.environ.get("DB_DB"),
        'user': os.environ.get("DB_USER"),
        'password': os.environ.get("DB_PASSWORD") ,
        'host': os.environ.get("DB_HOST"),
        'port': os.environ.get("DB_PORT")
    })

class DevelopmentConfig(Config):
    DEBUG=True