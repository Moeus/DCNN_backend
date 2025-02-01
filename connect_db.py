import mysql.connector

# 配置数据库连接信息
config = {
    'user': 'moeus',  # 替换为你的 MySQL 用户名
    'password': '923moeus',  # 替换为你的 MySQL 密码
    'host': 'localhost',  # 本地 MySQL 服务地址
    'port': 3306,  # MySQL 默认端口
    'database': 'DCNN'  # 替换为你要连接的数据库名
}

try:
    # 建立数据库连接
    connection = mysql.connector.connect(**config)
    if connection.is_connected():
        print('成功连接到 MySQL 数据库！')

        # 在这里可以进行数据库操作，例如创建游标、执行 SQL 语句等
        cursor = connection.cursor()
        cursor.execute('SELECT VERSION()')
        version = cursor.fetchone()
        print(f'MySQL 版本: {version[0]}')

        # 关闭游标和连接
        cursor.close()
        connection.close()
        print('数据库连接已关闭。')

except mysql.connector.Error as err:
    print(f'连接数据库时出现错误: {err}')