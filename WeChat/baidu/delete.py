from aip import AipImageSearch

""" 你的 APPID AK SK """
APP_ID = '11183322'
API_KEY = '8UF9PssmdeEM1CikKrnI78Tj'
SECRET_KEY = 'ourP7NkBa1Lbn84RCeSu4e39OC9Ttbm4'
client = AipImageSearch(APP_ID, API_KEY, SECRET_KEY)
""" 读取图片 """


contSign = "4043096407,707976548"

""" 调用删除相同图，传入参数为图片签名 """
print(client.similarDeleteBySign(contSign))
