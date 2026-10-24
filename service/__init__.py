"""Product catalogue service package."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.update(
        SQLALCHEMY_DATABASE_URI='sqlite:///products.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SECRET_KEY='dev-key-change-me',
    )
    if test_config:
        app.config.update(test_config)
    db.init_app(app)
    from service.models import Product
    from service.routes import bp
    app.register_blueprint(bp)
    with app.app_context():
        db.create_all()
    return app
