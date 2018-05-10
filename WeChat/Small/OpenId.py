import requests
import os

"""微信小程序获取openid"""
APP_ID = "wxea376b2867ed0b69"
APP_SECRET = "12c647a5761f2112a5dd00efd3633154"
OPENID_URL = "https://api.weixin.qq.com/sns/jscode2session?appid=APPID&secret=SECRET&js_code=JSCODE&grant_type=" \
             "authorization_code"


class openid(object):
    CODE = ""
    OPEN_ID = ""

    def openid(self):  # 获取openid

        url = OPENID_URL.replace("APPID", APP_ID).replace("SECRET", APP_SECRET).replace("JSCODE", CODE)
        res = requests.get(url)  # 进行get提交
        OpenId = res.json().get('openid')  # 获取的json直接是dict类型
        self.OPEN_ID = OpenId

    def setcode(self, Code):
        self.CODE = Code

    def getopenid(self):
        return self.OPEN_ID

    def mkdir(self):  # 创建用户模版，和类似图片文件夹
        File_Path = os.getcwd()[:-5] + 'image/' + self.OPEN_ID
        if not os.path.exists(File_Path):
            os.makedirs(File_Path+'/in')
            os.makedirs(File_Path+'/out')
