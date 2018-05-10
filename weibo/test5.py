import rk
import re
import time
import json
from selenium import webdriver
from urllib import request
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq

options = webdriver.ChromeOptions()
#   使用 headless 无界面浏览器模式
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
#   打开浏览器
browser = webdriver.Chrome(chrome_options=options)
wait = WebDriverWait(browser, 10)  # 显示加载



def code():
    rc = rk.RClient('1290259791', 'hu1997', '101476', 'a0546e49605d427790704b48b0221243')
    im = open('image.png', 'rb').read()
    code = rc.rk_create(im, 3040)
    return code.get('Result')


def login_in(user = None, password = None):
    url = 'http://172.16.154.130:8800'
    browser.get(url)

    input1 = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#loginform-username')))  # 获取输入框
    input2 = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#loginform-password')))  # 获取输入框
    input3 = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#loginform-verifycode')))
    submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#login-form > div:nth-child(6) > div.col-lg-10.col-lg-offset-1 > button')))  # 获取确定按钮

    geturl = json.load(request.urlopen('http://172.16.154.130:8800/site/captcha?refresh=1&_=1524368423294'))
    imageurl = 'http://172.16.154.130:8800' + geturl['url']
    getimage = request.urlopen(imageurl)
    imagefile = open('image.png', 'wb')
    imagefile.write(getimage.read())
    imagefile.close()

    input1.clear()
    input2.clear()
    input3.clear()
    input1.send_keys(user)
    input2.send_keys(password)
    time1 = time.time()
    getcode = code()
    print(time.time()-time1)

    input3.send_keys(getcode)
    submit.click()
    html = browser.page_source
    print(html)


login_in(201516070106, 'hu1997')





# rc = rk.RClient('1290259791', 'hu1997', '101476', 'a0546e49605d427790704b48b0221243')
# im = open('.png', 'rb').read()
# print(rc.rk_create(im, 3040))
