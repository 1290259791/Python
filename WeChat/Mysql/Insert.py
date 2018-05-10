import pymysql

"""数据添加操作"""


class insert(object):

    def __init__(self, sql):
        self.db = pymysql.connect(host='gz-cdb-5k17tpvi.sql.tencentcdb.com', port=62782, user='root',
                                  password='Shagua580231',
                                  db='WeChat')
        self.sql = sql

    def Insert(self):
        db = self.db
        cursor = self.db.cursor()
        try:
            cursor.execute(self.sql)
            db.commit()
            return True
        except:
            db.rollback()
            return False

    def close(self):
        self.db.close()


def openid(ID):
    openidsql = r"insert into user(openid) values('%s')" % ID
    openididinsert = insert(openidsql)
    openididinsert.Insert()
    openididinsert.close()


if __name__ == '__main__':
    sql = ""

