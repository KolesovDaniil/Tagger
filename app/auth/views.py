from typing import Dict
from datetime import timedelta
from flask_login import current_user, login_user, logout_user

from app.models import User, Text
from app.exceptions import UnauthorizedError, ValidationError
from app.database import db


def login(payload: Dict) -> None:
    """Try to log in user

    :raise UnauthorizedError: Raises when username or password is invalid
    """

    if not current_user.is_authenticated:
        user = db.session.query(User).filter(User.username == payload['username']).first()

        if user is None or not user.check_password(payload['password']):
            raise UnauthorizedError('Invalid username or password')

        login_user(user, remember=True, duration=timedelta(days=1))


def logout() -> None:
    """Log out user"""

    logout_user()


def registration(payload: Dict) -> None:
    """Register new user"""

    _check_fields_uniqueness(payload)
    user = User(username=payload['username'],
                email=payload['email'])
    user.set_password(payload['password'])

    db.session.add(user)
    db.session.commit()


def _check_fields_uniqueness(payload: Dict) -> None:
    """Check uniqueness constraints

    :raise ValidationError: Raises when uniqueness constraints is invalid
    """

    if db.session.query(User).filter(User.username == payload['username']).first():
        raise ValidationError('Field: (name) is not unique')

    if db.session.query(User).filter(User.email == payload['email']).first():
        raise ValidationError('User already exist with this email')
