"""ORM models"""

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

from app.database import db


class User(UserMixin, db.Model):
    """Пользователь"""

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False, unique=True)

    texts = db.relationship('Text', back_populates='owner')

    def set_password(self, password):
        """"""

        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """"""

        return check_password_hash(self.password_hash, password)


class Text(db.Model):
    """Текст"""

    __tablename__ = 'text'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String, nullable=False)
    creation_dt = db.Column(db.DateTime, nullable=False)
    last_update_dt = db.Column(db.DateTime)
    tags = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    owner = db.relationship('User',
                            back_populates='texts')
