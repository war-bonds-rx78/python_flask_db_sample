from flask import Blueprint, jsonify
from api.service.jwt import encode_jwt_service

# Blueprintのオブジェクトを生成する
app = Blueprint('encode_jwt', __name__)


@app.route('/')
def get():
    jwt = encode_jwt_service.EncodeJwtService()
    ret = jwt.execute()
    return jsonify(ret)
