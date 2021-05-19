import os
import logging
from logging import handlers

# テキスト形式で出力するログファイル
# 出力は、各メソッド内で実施


class Api_logger():
    def __init__(self, name):
        super().__init__()
        # ログ取得
        self.log = logging.getLogger(name)
        if not self.log.hasHandlers():
            # ログレベル
            self.log.setLevel(logging.INFO)
            # フォーマットとハンドラー
            # ベースパス取得
            bath_pash = os.getcwd()
            # 日付ローテーションおよび7日
            file_handler = logging.handlers.TimedRotatingFileHandler(
                filename=bath_pash + '/log/app.log', encoding='UTF-8', when='MIDNIGHT', backupCount=7)
            # ログフォーマット設定
            format_str = logging.Formatter(
                '%(asctime)s - [%(levelname)s] - %(name)s  - %(funcName)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(format_str)
            self.log.addHandler(file_handler)

    def getLogger(self):
        return self.log
