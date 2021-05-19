from datetime import datetime
from api.common.db.setting import db


class User(db.Model):

    __tablename__ = 'users'

    user_id = db.Column(db.String(255), primary_key=True)
    password = db.Column(db.String(255), nullable=False)
    user_name = db.Column(db.String(255), nullable=False)
    insert_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def getUserList(self):
        list = db.session.query(User).all()

        for data in list:
            print(data.user_id)
            print(data.password)
            print(data.user_name)
            print(data.insert_date)
            print(data.update_date)

        return list
