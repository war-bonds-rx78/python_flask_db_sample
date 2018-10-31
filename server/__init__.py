from flask import Flask
from server.api import todo_view, todo_add
from server.config import db_config

## アプリケーション初期
def init_app():
    ## アプリケーション生成
    application = Flask(__name__, instance_relative_config=True)
    ## ルート定義
    blueprints = [todo_view.app, todo_add.app]
    for blueprint in blueprints:
        application.register_blueprint(blueprint, url_prefix='/')

    return application

application = init_app()

