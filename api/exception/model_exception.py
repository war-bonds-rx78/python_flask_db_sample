import traceback

# モデル例外


class ModelException(Exception):
    # コンストラクタ
    def __init__(self, e):
        self.e = e

    # エラーメッセージ詳細
    def getErrMsgDetails(self):
        return traceback.format_exc()

    # エラーメッセージのみ
    def getErrMsg(self):
        return traceback.format_exception_only(type(self.e), self.e)
