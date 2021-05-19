import jwt


class EncodeJwtService():
    def __init__(self):
        super().__init__()

    def execute(self):

        param = {}
        private_key = "test"
        encode = jwt.encode({"some": "payload"},
                            private_key, algorithm="HS256")

        param['key'] = encode
        return param
