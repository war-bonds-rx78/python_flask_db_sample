import os
from flask import Blueprint, jsonify, current_app
from api.common import message

# Blueprintのオブジェクトを生成する
app = Blueprint('sample', __name__)


@app.route('/')
def get():

    re_dict = {}
    re_dict['name'] = "こんにちは"
    re_dict['config'] = current_app.config['SAMPLE']

    ms = message.Message()
    re_dict['path'] = ms.get('MSG', 'INFO_N001')
    # jsonifyが返却値をjson形式に変換してくれる
    return jsonify(re_dict)
