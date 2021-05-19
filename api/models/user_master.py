from api.common.db.setting import db
from sqlalchemy import text
from api.models import manual_model


class UserMaster(manual_model.ManualModel):

    def __init__(self):
        super().__init__(db)

    def get(self):
        sql = text('select * from type_master')
        with db.engine.connect() as con:
            result = con.execute(sql)

            print('内部確認')
            for data in result:
                print(type(data))

        return list

    # insert文
    def execute_insert_type_master(self):
        # %(パラメータのキー名)s
        sql = "INSERT INTO type_master(name) VALUES(%(name)s);"
        return sql

    # アップデート文
    def execute_update_type_master(self):
        sql = "UPDATE type_master set name=%(name)s where id =%(id)s;"
        return sql
