from server.config.db_config import Session

# セッション生成
def begin():
    return Session()

# セッション終了
def close(session):
    session.close()

# コミット
def commit(session):
    session.commit()