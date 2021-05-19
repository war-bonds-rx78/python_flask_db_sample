from flask import Blueprint, jsonify, request
from api.service.hoge import hoge_service
from api.common import logger
from api.common import logger_json

# Blueprintのオブジェクトを生成する
app = Blueprint('hoge', __name__)


@app.route('/', methods=['GET'])
def get_all():

    log = logger.Api_logger("hoge")
    json_log = logger_json.Api_logger_json("hoge")

    log.getLogger().info("開始")

    service = hoge_service.Hoge()

    re = service.execute()

    log.getLogger().info("終了")
    json_log.getLogger().info(
        'テスト', extra={'sample': 'a', 'test1': 'data', 'test2': 'sample'})
    # jsonifyが返却値をjson形式に変換してくれる
    return jsonify(re)


@app.route('/<id>', methods=['GET'])
def get_id(id):
    kind = request.args.get('kind')

    re = {}
    re['id'] = id
    re['kind'] = kind

    return jsonify(re)


@app.route('/', methods=['POST'])
def post():

    print(type(request.json))
    print(request.json['key'])
    re = {}
    re['status'] = 'OK'

    return jsonify(re)


@app.route('/<id>', methods=['PUT'])
def put(id):
    re = {}
    re['status'] = 'OK'

    print(id)
    print(type(request.json))
    print(request.json['key'])

    return jsonify(re)


@app.route('/<id>', methods=['DELETE'])
def delete(id):
    re = {}
    re['status'] = 'OK'

    print(id)

    return jsonify(re)
