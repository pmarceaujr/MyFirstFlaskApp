
from app import create_app, db
from app.auth.models import User
from sqlalchemy import exc

if __name__ == '__main__':
    flask_app = create_app('dev')
    with flask_app.app_context():
        print("do db")
        db.create_all()
        try:
            if not User.query.filter_by(user_name='harry').first():
                User.create_user(user='harry', email='harry@potters.com', password='secret')
        except exc.IntegrityError:
            pass
    flask_app.run()
