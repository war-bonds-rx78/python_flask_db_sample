from datetime import datetime
from api.common.db.setting import db


class TypeMaster(db.Model):

    __tablename__ = 'type_master'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

    def getList(self):
        list = db.session.query(TypeMaster).all()

        for data in list:
            print(data.id)
            print(data.name)

        return list
