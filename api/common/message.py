# メッセージ
# カレンパス取得
# configフォルダからymlを読み込み
import os
import yaml


class Message():

    def __init__(self):
        super().__init__()
        bath_pash = os.getcwd()

        with open(bath_pash + '/config/message.yml', 'r') as yml:
            self.config = yaml.safe_load(yml)

    def get(self, indent1, indent2):
        return self.config[indent1][indent2]
