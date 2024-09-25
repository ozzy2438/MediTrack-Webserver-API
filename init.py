from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()
migrate = Migrate()

def init_app(app):
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    return app
