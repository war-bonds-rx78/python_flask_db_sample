
# postgres設定
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}'.format(**{
    'user': 'test01',
    'password': 'test01',
    'host': '127.0.0.1',
    'port': '15432',
    'name': 'test01'
})
