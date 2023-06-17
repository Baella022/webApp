from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1gh2gh3gh'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pikininiscienceapp.db'

    db.init_app(app)

    from .views import views
    app.register_blueprint(views)

    login_manager.init_app(app)
    login_manager.login_view = 'views.login'

    return app
