from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    print(app.config["TEST_VAR"])

    return app

