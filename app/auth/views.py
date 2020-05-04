from typing import Dict
from datetime import timedelta
from flask_login import current_user, login_user, logout_user

from app.models import User
from app.exceptions import UnauthorizedError
from app.database import db


def login(payload: Dict):
    """"""

    if not current_user.is_authenticated:
        user = db.session.query(User).filter(User.username == payload['username']).first()

        if user is None or not user.check_password(payload['password']):
            raise UnauthorizedError('username or password is incorrect')

        login_user(user, remember=True, duration=timedelta(days=1))


def logout():
    """"""

    logout_user()
