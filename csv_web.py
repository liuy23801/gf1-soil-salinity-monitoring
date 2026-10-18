import json
import pandas as pd
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index02():

    return render_template('index02.html')

@app.route('/data')
def get_data():
    df = pd.read_csv('热力图.csv')

    # 转换为JSON格式
    json_data = df.to_json(orient='records')

    # 解析 JSON 字符串为 Python 对象
    parsed_json_data = json.loads(json_data)

    return jsonify(parsed_json_data)

if __name__ == '__main__':
    app.run(debug=True)