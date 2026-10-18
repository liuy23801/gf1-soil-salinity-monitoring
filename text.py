import json
import pandas as pd
from flask import Flask, render_template, request, jsonify
import pymysql
import subprocess
import numpy as np
from rasterio.plot import show
from rasterio.io import MemoryFile
import cv2
import rasterio

import geopandas as gpd

app = Flask(__name__)

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/index01")
def index01():
    return render_template('index01.html')

@app.route("/index02")
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


def radiometric_calibration(image, gain, offset):
    calibrated_image = image * gain + offset
    return calibrated_image

def atmospheric_correction(image, atmospheric_transmission):
    corrected_image = image / atmospheric_transmission
    return corrected_image

@app.route("/index03")
def index03():

     return render_template('index03.html')
#     print(f"影像辐射校正完成，结果已输出到本文件夹下")
#
# # 读取GF-1影像
#     image = cv2.imread('Kerle11.tif', cv2.IMREAD_GRAYSCALE)
# # 辐射定标
#     gain = 0.5
#     offset = 10
#     calibrated_image = radiometric_calibration(image, gain, offset)
# # 大气校正
#     atmospheric_transmission = 0.8
#     corrected_image = atmospheric_correction(calibrated_image, atmospheric_transmission)
# # 保存校正后的影像
#     cv2.imwrite('corrected_image.tif', corrected_image)
#     return render_template('index03.html')


@app.route("/index04")
def index04():
    # img_path = 'H:\pythontext\images\Figure_1.png'
    # img_stream = return_img_stream(img_path)
    return render_template('index04.html')

@app.route("/index05")
def index05():
    return render_template('index05.html')

@app.route("/index06")
def index06():
    NDSI = '0.15556589013432598'
    NDVI = '0.45369587319432698'
    SI= '0.5954910939805613'
    SI_T='0.9458643517865306'
    SAVI='0.14656918880376457'
    BI='0.5117179059894994'
    SI1='0.47124200788960513'
    SI2='0.45186242299938284'
    SI3='0.4763116127657585'
    S1='0.6774201335924279'
    S2='0.5913043218683356'
    S3='0.3373517671897963'
    S5='0.8243571686976436'
    S6='0.4344279380292504'
    Int1='0.4738536964065587'
    Int2='0.45217745694529743'
    b1='0.0011337995732241257'
    b2='0.006179220760406112'
    b3='0.09343454638139348'
    b4='0.0392461451514281'
    return render_template('index06.html',
                           NDSI=NDSI,
                           NDVI=NDVI,
                           SI=SI,
                           SI_T=SI_T,
                           SAVI=SAVI,
                           BI=BI,
                           SI1=SI1,
                           SI2=SI2,
                           SI3=SI3,
                           S1=S1,
                           S2=S2,
                           S3=S3,
                           S5=S5,
                           S6=S6,
                           Int1=Int1,
                           Int2=Int2,
                           b1=b1,
                           b2=b2,
                           b3=b3,
                           b4=b4)


@app.route("/index07")
def index07():
    return render_template('index07.html')

#---------------------------------------------------------------------------------------测试
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return "No file part"
#     file = request.files['file']
#     if file.filename == '':
#         return "No selected file"
#     if file:
#         filename = file.filename
#         file.save('/path/to/upload/' + filename)
#         return "File uploaded successfully"
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        # 这里可以添加保存文件的代码
        filename = file.filename
        return "File {} uploaded successfully".format(filename)

@app.route('/run-python-script', methods=['POST'])
def run_python_script():
    # 这里调用Python脚本的命令
    result = subprocess.run(['python', 'GF1.py'], capture_output=True, text=True)

    # 检查脚本是否成功执行
    if result.returncode == 0:
        print("Python脚本执行成功")
    else:
        print("Python脚本执行失败，错误代码:", result.returncode)
    # 返回结果
    # return jsonify({'stdout': result.stdout, 'stderr': result.stderr})

@app.route('/runPython_tubiaoButton', methods=['POST'])
def runPython_tubiaoButton():
    # 这里调用Python脚本的命令
    result = subprocess.run(['python', 'tubiao.py'], capture_output=True, text=True)

    # 检查脚本是否成功执行
    if result.returncode == 0:
        print("Python脚本执行成功")
    else:
        print("Python脚本执行失败，错误代码:", result.returncode)

@app.route('/runPython_tubiao1Button', methods=['POST'])
def runPython_tubiao1Button():
    # 这里调用Python脚本的命令
    result = subprocess.run(['python', 'tubiao1.py'], capture_output=True, text=True)

    # 检查脚本是否成功执行
    if result.returncode == 0:
        print("Python脚本执行成功")
    else:
        print("Python脚本执行失败，错误代码:", result.returncode)

@app.route('/runPython_tubiao2Button', methods=['POST'])
def runPython_tubiao2Button():
    # 这里调用Python脚本的命令
    result = subprocess.run(['python', 'tubiao2.py'], capture_output=True, text=True)

    # 检查脚本是否成功执行
    if result.returncode == 0:
        print("Python脚本执行成功")
    else:
        print("Python脚本执行失败，错误代码:", result.returncode)

@app.route('/runPython_chuliButton', methods=['POST'])
def runPython_chuliButton():
    # 这里调用Python脚本的命令
    result = subprocess.run(['python', 'Cut.py'], capture_output=True, text=True)

    # 检查脚本是否成功执行
    if result.returncode == 0:
        print("Python代码执行成功")

@app.route('/runPython_tifshpButton', methods=['POST'])
def runPython_tifshpButton():
    # 这里调用Python脚本的命令
    result = subprocess.run(['python', 'tif-shp.py'], capture_output=True, text=True)

    # 检查脚本是否成功执行
    if result.returncode == 0:
        print("Python代码执行成功")

@app.route('/runPython_shpresultButton', methods=['POST'])
def runPython_shpresultButton():
    # 这里调用Python脚本的命令
    result = subprocess.run(['python', 'shp.py'], capture_output=True, text=True)

    # 检查脚本是否成功执行
    if result.returncode == 0:
        print("Python代码执行成功")



@app.route("/login")
def login1():
    return render_template('login.html')
#
# @app.route("/index01")
# def index01():
#     return render_template('index01.html')
# 封装SQL语句函数
def func(sql, m='r'):
    py = pymysql.connect (host='localhost',  # 主机名
            user='root',  # 用户名
            password='YOUR_MYSQL_PASSWORD',  # 密码
            database='flask',# 数据库名
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor)
    cursor = py.cursor ()
    try:
        cursor.execute (sql)
        if m == 'r':
            data = cursor.fetchall()
        elif m == 'w':
            py.commit ()
            data = cursor.rowcount
    except:
        data = False
        py.rollback ()
    py.close ()
    return data


# 首页,将mysql中表的值读出并传到网页----查
@app.route ('/sqldata')
def index1():
    data = func ('select * from si')
    return render_template ('sqldata.html', userlist=data)


# 返回到添加操作的界面
@app.route ("/add/")
def ad():
    return render_template ('add.html')


# 接受添加的数据,写入数据库----增
@app.route ("/adds/", methods=["POST"])  # 注意post大写,因为post是通过form.data传数据所以下面用request.form
def adds():
    data = dict (request.form)
    print (data)
    sql = "insert into si values ('{Id}','{采样地}','{有机质}','{全氮}','{总磷}','{含水率}','{全钾量}','{水溶性盐_1}','{X}','{Y}')".format (**data)
    res = func (sql,m='w')
    if res:
        return '<script>alert("添加成功");location.href="/";</script>'
    else:
        return '<script>alert("添加失败");location.href="/";</script>'


# 返回到更改界面
@app.route ('/cha')
def ch():

    idd = request.args.get ('Id')
    data = func (f'select * from si where Id={idd}')
    return render_template ('cha.html',userlist=data)


# 检察更改的数据并更新数据库----改
@app.route ('/chas', methods=["POST"])
def chas():
    data = dict (request.form)
    res = func ("update si set Id='{Id}',采样地='{采样地}',有机质='{有机质}',全氮='{全氮}',总磷='{总磷}',含水率='{含水率}',全钾量='{全钾量}',水溶性盐_1='{水溶性盐_1}',X='{X}',Y='{Y}' where id={id}" .format (**data),
                m='w')
    if res:
        return '<script>alert("更新成功");location.href="/";</script>'
    else:
        return '<script>alert("未更新");location.href="/";</script>'


# 删除数据----删
@app.route ('/del')
def de():
    id = request.args.get('Id')
    res = func (f'delete from si where Id={id}',m='w')
    if res:
        return '<script>alert("删除成功");location.href="/";</script>'
    else:
        return '<script>alert("删除失败");location.href="/";</script>'


# @app.route('/process_form', methods=['POST'])
# def process_form():
#     name = request.form['name']
#     # 调用 Python 函数
#     result = my_python_function(name)
#     return result

# def my_python_function(name):
#     # 在这里编写你的 Python 函数逻辑
#     return 'Hello, ' + name + '!'


if __name__ == '__main__':
    app.run(port=5000,host="127.0.0.1",debug=True)