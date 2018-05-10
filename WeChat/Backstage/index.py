from flask import Flask, request

import OpenId
import Insert
import Select
import add
import os
app = Flask(__name__)


@app.route('/')
def index():
    return "hello word"


"""获取并检查数据库openid"""


@app.route('/openid', methods=['GET'])
def openid():
    Code = request.args.get('code')  # 获取Code
    OpenId.openid.setcode(OpenId, Code)     # 传入COde
    OpenId.openid.openid(OpenId)    # 执行获取Openid
    if not Select.openid(OpenId.openid.getopenid(OpenId)):  # 查询数据库有没有openid
        Insert.openid(OpenId.openid.getopenid(OpenId))
        OpenId.openid.mkdir(OpenId)
    return 'ok'


"""picture提交页面"""


@app.route('/picture', methods=['POST'])
def register():
    FileUrl = os.getcwd()[:-9] + 'Backimage/' + OpenId.openid.getopenid(OpenId)+'/in/1.png'    # 用户文件夹下的目录
    request.files.get('file').save(FileUrl)  # 保存图片到本地
    baidu = add.baidu()
    return 'ok' if baidu.image_add(FileUrl) else 'no'


"""picture寻找页面"""


@app.route('/picture1', methods=['POST'])
def searchpicture():
    FileUrl = os.getcwd()[:-9] + 'Backimage/' + OpenId.openid.getopenid(OpenId) + '/out/1.png'  # 用户文件夹下的目录
    request.files.get('file').save(FileUrl)  # 保存图片到本地
    baidu = add.baidu()
    result = baidu.image_search(FileUrl)
    return 'ok' if result is True else 'no'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
