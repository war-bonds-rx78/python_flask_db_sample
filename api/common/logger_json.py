import os
import logging
from logging import handlers
from api.common.jsonFormatter import JsonFormatter

# json形式で出力するログファイル


class Api_logger_json():
    def __init__(self, name):
        super().__init__()

        # ログ取得
        self.log = logging.getLogger(name + "_json")

        if not self.log.hasHandlers():
            # ログレベル
            self.log.setLevel(logging.INFO)
            # handrer追加
            # ベースパス取得
            bath_pash = os.getcwd()
            # 日付ローテーションおよび7日
            # jsonにする場合、日本語が文字化けするのでライブライリーを修正する必要がある
            # 「json_log_formatter」ディレクトリ内の「__init__.py」の「to_json」のreturnメソッドに
            #  [, ensure_ascii=False]を追加
            # ライブラリの場所は、[pip show パッケージ名]でわかる
            file_handler = logging.handlers.TimedRotatingFileHandler(
                filename=bath_pash + '/log/app_json.log', encoding='UTF-8', when='MIDNIGHT', backupCount=7)
            # 日本語出力対応
            formatter = JsonFormatter(json_ensure_ascii=False)
            file_handler.setFormatter(formatter)
            self.log.addHandler(file_handler)

    def getLogger(self):
        return self.log
