from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    print(app.config["TEST_VAR"]) # confirms that variables are being loaded

    from flask_app_demo.main.routes import main
    app.register_blueprint(main)

    return app

