from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    with app.app_context():
        from . import routes, authentication, remittance, payment
        app.register_blueprint(routes.bp)
        app.register_blueprint(authentication.bp)
        app.register_blueprint(remittance.bp)
        app.register_blueprint(payment.bp)

        return app
