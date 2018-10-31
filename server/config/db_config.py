from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from server.models.models import Base

def init_db():

    # テーブル作成
    engine = create_engine("sqlite:///db/sample.db")
    Base.metadata.create_all(engine)
    # セッション設定
    Session = sessionmaker(bind=engine)

    return Session

Session = init_db()