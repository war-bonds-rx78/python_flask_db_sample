from flask import Blueprint, jsonify, request
from api.service.jwt import decode_jwt_service

# Blueprintのオブジェクトを生成する
app = Blueprint('decode_jwt', __name__)


@app.route('/')
def get():

    auth = request.headers.get("x-Authentication")

    jwt = decode_jwt_service.DecodeJwtService()
    ret = jwt.execute(auth)
    return jsonify(ret)
