from api.exception.model_exception import ModelException
from sqlalchemy import text
import traceback


class ManualModel():

    def __init__(self, db):
        self.databese = db

    def execute(self, sql_str, param):

        sql = text(sql_str)
        with self.databese.engine.begin() as con:
            # SQL定義したキーと一致してること
            try:
                result = con.execute(sql_str, param)
            except Exception as e:
                # ERR ログ出力
                # エラー全体をキャッチ
                # エラー内容全体
                #t = traceback.format_exc()
                # 明示しなくてもwith内であれば例外発生で自動rollbackがかかる
                # con.connection.rollback()
                # オリジナル例外
                raise ModelException(e)

            if result.rowcount == 0:
                # ERR ログ出力
                # 更新件数できない場合
                raise Exception
