import solution
from flask import Flask, request,send_from_directory
import json
import os
app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    # 从static目录中发送robot.png文件作为favicon
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'robot.png', mimetype='image/png')
@app.route('/', methods=['GET'])
def home():
    return "Hello World"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    print("成功接受到post请求")
    result = solution.solve(data)
    print("请求处理完成，正在返回")
    return json.dumps(result)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
