# 2021 版 flask アプリテンプレート

## やること

- yml の confg - 完了
  - log 設定
    - python の logger を使用して作成
      - 残
        - ファイル出力
        - logger 名固定
        - 保留
        - json 形式として出力
          - フォーマット見直し
            - メソッド化
            - 時間が日本時間に修正
  - ORM の使用した SQL 接続
    - 2 パターンを実施したが、model 定義だと学習コストが高い
    - 例として作っているが、実際は SQL 文を自分で作るやり方でこのテンプレートモジュールは作っていく
  - 独自例外
    - 完了 model_execption
  - jwt
    - HS256 簡易
      - 一旦放置
  - PUT,POST,DEL 対応
    - hoge の controller に記載
    - put と post の切り分け
  - WSGI 対応（本番環境想定）
    - 別プロジェクトに移動
  - init 化

## 導入パッケージ

- Flask
- PyYAML
- Flask-SQLAlchemy
- Flask-Migrate
- SQLAlchemy
- psycopg2-binary
- requests
- Flask-JWT-Extended
- python-json-logger

## TODO

- DB 処理を綺麗にする
- マニュアル方式
- テストケース作成
