from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    db.init_app(app)

    from flask_app_demo.main.routes import main
    app.register_blueprint(main)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    return app

