""""""

from flask_migrate import Migrate

from app.factory import create_app
from app.database import db
from app.login import login


app = create_app()
app.secret_key = 'the random string'
migrate = Migrate(app, db)
login.init_app(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6060)
