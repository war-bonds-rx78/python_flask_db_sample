from flask import Flask, request
from api.controller.sample import sample
from api.controller.hoge import hoge
from api.controller.jwt import encode_jwt
from api.controller.jwt import decode_jwt
from api.common import logger
from api.common.db.setting import init_db


app = Flask(__name__, instance_relative_config=True)

# config設定読み込み
app.config.from_pyfile('config.py')


# 分割したblueprintを登録する
app.register_blueprint(sample.app, url_prefix='/v1/sample')
app.register_blueprint(hoge.app, url_prefix='/v1/hoge')
app.register_blueprint(encode_jwt.app, url_prefix='/v1/encode_jwt')
app.register_blueprint(decode_jwt.app, url_prefix='/v1/decode_jwt')
init_db(app)


@app.before_request
def before_request():
    log = logger.Api_logger(__name__)
    log.getLogger().info("フィルタ")
    log.getLogger().info(request.path)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
