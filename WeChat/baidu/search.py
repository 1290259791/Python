from aip import AipImageSearch

""" 你的 APPID AK SK """
APP_ID = '11183322'
API_KEY = '8UF9PssmdeEM1CikKrnI78Tj'
SECRET_KEY = 'ourP7NkBa1Lbn84RCeSu4e39OC9Ttbm4'

client = AipImageSearch(APP_ID, API_KEY, SECRET_KEY)
""" 读取图片 """


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content('7.png')

options = {"tags": "100,1", "pn": "0", "rn": "7"}
""" 带参数调用相似图检索—检索 """
result = client.similarSearch(image, options)
for line in result.get('result'):
    print(line)
