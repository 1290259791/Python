from urllib import request
import json

# client_id 为官网获取的AK， client_secret 为官网获取的SK
API_Key = '8UF9PssmdeEM1CikKrnI78Tj'
Secret_key = 'ourP7NkBa1Lbn84RCeSu4e39OC9Ttbm4'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + API_Key + \
       '&client_secret=' + Secret_key

req = request.Request(host)
req.add_header('Content-Type', 'application/json; charset=UTF-8')
response = request.urlopen(req)
content = response.read()
text = json.loads(content)  # 获取 Token 值格式化 JSON
print(text)
