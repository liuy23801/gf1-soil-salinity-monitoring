import json
from flask import Flask,jsonify,Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import pymysql
app = Flask(__name__)
db = pymysql.connect(
            host='localhost',  # 主机名
            user='root',  # 用户名
            password='YOUR_MYSQL_PASSWORD',  # 密码
            database='flask'  # 数据库名
        )
cursor =db.cursor()

def select_si():
    sql = 'select * from si'
    cursor.execute(sql)
    data = cursor.fetchall()
    return data


@app.route("/")
def select_user_si():
    data = select_si()
    dicts={"data":[]}
    for i in data:
        dicts['data'].append(i)
    json_data = json.dumps(dicts,ensure_ascii=False)
    return Response(json_data, content_type='application/json')

# @app.route('/addnum',method=['GET','POST'])
# def register():
#     print(request.method)
#     if request.method =='GET':
#         return render_template('')
#
#     print(request.form)
#
#     #取值
#     username = request.form.get('username')

if __name__ == '__main__':
     app.run(port=8888)



