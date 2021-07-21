from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///board.db"
# DB를 지정 + 파일명을 지정. 작대기 3개면 상대경로, 4개면 절대경로
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['JSON_AS_ASCII'] = False

db = SQLAlchemy(app)
db.init_app(app)

if __name__ == '__main__':
    app.run(port=1234, debug=True)