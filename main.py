import pymysql

# 创建数据库连接
conn = pymysql.connect(
    host='localhost',# 连接主机, 默认127.0.0.1
    user='root',      # 用户名
    passwd='YOUR_MYSQL_PASSWORD',
    port=3306,        # 端口，默认为3306
    db='flask',        # 数据库名称
    charset='utf8'    # 字符编码
)

# 生成游标对象 cursor
cursor = conn.cursor()

#查询数据库版本
cursor.execute("select version()") # 返回值是查询到的数据数量
# 通过 fetchall方法获得数据
data = cursor.fetchone()
print("Database Version:%s" % data)

# 数据库查询数据

sql = "SELECT * FROM si"
cursor.execute(sql) # 返回值是查询到的数据数量
data = cursor.fetchall() # 查询一条数据
print("显示全部数据：", data)

# 查询指定条件的数据
sql = " SELECT * FROM si WHERE 含水率 >= '%d' " % (263.88)
cursor.execute(sql)# 返回值是查询到的数据数量
data = cursor.fetchall()
print(data)

cursor.close()  # 关闭游标
conn.close()    # 关闭连接
