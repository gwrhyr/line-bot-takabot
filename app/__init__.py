import os
from flask import Flask
from sqlalchemy_utils import create_database, database_exists

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_object("app.config.DevelopmentConfig")

#    if app.config["FLASK_ENV"] == "development":
#        app.config.from_pyfile(os.path.join("config", "development.py"), silent=True)
#    else:
#        app.config.from_pyfile(os.path.join("config", "production.py"), silent=True)

    if test_config is not None:
        app.config.from_mapping(test_config)

    db_url = app.config["SQLALCHEMY_DATABASE_URI"]
    if not database_exists(db_url):
        create_database(db_url)
    
    return app