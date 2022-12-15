
from app import create_app, db

if __name__ == '__main__':
    flask_app = create_app('dev')
    with flask_app.app_context():
        print("do db")
        db.create_all()
    flask_app.run()
