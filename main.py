from flask import Flask
from flask_migrate import Migrate
from website import create_app, db
from website.views import views

app = create_app()
app.register_blueprint(views, name='main_views')

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)
else:
    gunicorn_app = app
