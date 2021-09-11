from sqlalchemy.pool import QueuePool
from instance.postgressql import SQLALCHEMY_DATABASE_URI as DATABASE_URI

# flask用固有定義
# デバックもーど
DEBUG = True
# テストモード
TESTING = False
# 日本語か対応
JSON_AS_ASCII = False
# システム用定義
SAMPLE = '設定値'

# DB設定
#SECRET_KEY = '\xf7\xf4\x9bb\xd7\xa8\xdb\xee\x9f\xe3\x98SR\xda\xb0@\xb7\x12\xa4uB\xda\xa3\x1b'
#STRIPE_API_KEY = ''
SQLALCHEMY_DATABASE_URI = DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_ENGINE_OPTIONS = {
    "poolclass": QueuePool,
    'pool_size': 5,
    'max_overflow': 15,
    'pool_recycle': 120,
    'pool_pre_ping': True
}
