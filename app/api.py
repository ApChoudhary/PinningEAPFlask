from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from sqlConnection import getData, insertData
import datetime

app = Flask(__name__)
app.secret_key = 'test'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)

jwt = JWT(app, authenticate, identity)

@app.route('/')
@cross_origin()
@jwt_required()
def hello_world():
    return jsonify('Hello World!')

@app.route('/dbdata', methods=['POST'])
def dbData():
    print('test')
    data = request.get_json()
    return jsonify(getData(data))

@app.route('/insertIntoDB', methods=['POST'])
def insertIntoDb():
    print("hello noob")
    data = request.get_json()
    insertData(data)
    return "insert"


if __name__ == '__main__':
    app.debug = True
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.run()