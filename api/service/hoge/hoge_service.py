from api.exception.model_exception import ModelException
from api.models import typeMaster
from api.models import user_master
# from api.models import user


class Hoge():

    def __init__(self):
        super().__init__()

    def execute(self):
        re_dict = {}
        re_dict['name'] = "おやすみ"

        db = typeMaster.TypeMaster()
        hogelist = db.getList()

        for hoge in hogelist:
            print('*******')
            print(hoge.name)

        test = user_master.UserMaster()
        test.get()
        # db_user = user.User()
        # db_user.getUserList()

        #sql = test.insert_type_master()
        sql = test.execute_update_type_master()
        param = {}
        param['name'] = "12345"
        param['id'] = 17
        try:
            test.execute(sql, param)
        except ModelException as e:
            msg = e.getErrMsgDetails()
            print("*****")
            print(msg)
            print("*****")
            print(e.getErrMsg())
            print("------")

        return re_dict
