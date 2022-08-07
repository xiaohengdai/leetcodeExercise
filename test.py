from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():

    #请求飞书的东西
    #得到它的响应数据
    #自己进行数据处理后返给飞书
    name = 'world'
    if 'name' in request.args:
        name = request.args['name']
    data = {'data': 'hello ' + name}
    return jsonify(data)


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(port=5002)