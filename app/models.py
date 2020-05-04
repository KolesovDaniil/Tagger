"""ORM models"""

from app.database import db


class User(db.Model):
    """Пользователь"""

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)

    text = db.relationship('Text', backref='user')


text_x_tag = db.Table('text_x_tag',
                      db.Column('text_id', db.Integer,
                                db.ForeignKey('text.id'),
                                primary_key=True),
                      db.Column('tag_name', db.String,
                                db.ForeignKey('tag.name'),
                                primary_key=True)
                      )


class Text(db.Model):
    """Текст"""

    __tablename__ = 'text'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String, nullable=False)
    creation_dt = db.Column(db.DateTime, nullable=False)
    last_update_dt = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    text_tags = db.relationship('Tag',
                                secondary=text_x_tag,
                                backref='texts')


class Tag(db.Model):
    """Тег"""

    __tablename__ = 'tag'

    name = db.Column(db.String, primary_key=True)

    texts_with_tag = db.relationship('Text',
                                     secondary=text_x_tag,
                                     backref='tags')
