import jwt


class DecodeJwtService():

    def __init__(self):
        super().__init__()

    def execute(self, encoded):
        key = "test"
        key = jwt.decode(encoded, key, algorithms="HS256")
        re = {}
        re['key'] = key

        return re
