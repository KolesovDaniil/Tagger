"""Log in module"""

from flask_login import LoginManager, current_user

from app.models import User
from app.database import db
from app.exceptions import UnauthorizedError


login = LoginManager()
login.login_view = 'api_bp.unauthorized_error_handler'


@login.user_loader
def load_user(id: int):
    return db.session.query(User).filter(User.id == id).first()
