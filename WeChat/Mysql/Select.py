import pymysql

"""数据库查找操作"""


class select(object):
    def __init__(self, sql):
        self.db = pymysql.connect(host='gz-cdb-5k17tpvi.sql.tencentcdb.com', port=62782, user='root',
                                  password='Shagua580231',
                                  db='WeChat')
        self.sql = sql

    def Select(self):
        cursor = self.db.cursor()
        try:
            cursor.execute(self.sql)
            result = cursor.fetchone()
            if result[0]:
                return True
        except:
            return False

    def Close(self):
        self.db.close()


def openid(ID):
    openidsql = r"select * from user where openid = '%s'" % ID
    openidselect = select(openidsql)
    result = openidselect.Select()      # 存在的时候返回True
    openidselect.Close()
    return result


if __name__ == '__main__':
    pass