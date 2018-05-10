from aip import AipImageSearch
import time

""" 读取图片 """


def get_file_content(filePath):  # 将图片二进制读取
    with open(filePath, 'rb') as fp:
        return fp.read()


class baidu(object):
    """ 你的 APPID AK SK """
    APP_ID = '11183322'
    API_KEY = '8UF9PssmdeEM1CikKrnI78Tj'
    SECRET_KEY = 'ourP7NkBa1Lbn84RCeSu4e39OC9Ttbm4'

    def __init__(self):
        self.client = AipImageSearch(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    def image_add(self, filename):  # 添加
        image = get_file_content(filename)
        options = {"tags": "100,1", "brief": "{\"name\":\"test4\"}"}  # tags是进行二维分组
        result = self.client.similarAdd(image, options)  # 调用参数入库
        return False if result.get('error_code') else True

    def image_search(self, filename):  # 搜索
        image = get_file_content(filename)
        options = {"tags": "100,1", "pn": "0", "rn": "1"}  # tages在二维分组里查找，pn是分页，rn是截取条数
        result = self.client.similarSearch(image, options)
        for line in result.get('result'):   # 检查第一个返回的
            pass
        if int(line.get('score')) > 0.8:    # 相似度大于0.8返回相同
            return True
        else:
            return False

    def image_delete(self, contSign):  # 删除
        # contSign = "385018571,3552852085"
        self.client.similarDeleteBySign(contSign)


if __name__ == '__main__':
    time1 = time.time()
    bd = baidu()
    # bd.image_search('7.png')
    print(bd.image_add('7.png'))
    print(time.time() - time1)
