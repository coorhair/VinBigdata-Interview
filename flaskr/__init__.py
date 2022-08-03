import os
from flask import Flask
from pymongo.errors import DuplicateKeyError


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        MONGO_URI='mongodb://mongodb:27017/vinbigdata_interview'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from .error_handling import handle_duplicate_key, handle_404
    app.register_error_handler(404, handle_404)
    app.register_error_handler(DuplicateKeyError, handle_duplicate_key)

    from .api import mobile_api_v1
    app.register_blueprint(mobile_api_v1)

    from . import db
    db.init_app(app)

    return app
