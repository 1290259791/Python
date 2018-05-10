from selenium import webdriver
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


def index_page(user, password):

    url = 'https://ffis.me/jiaowu/weblogin/fuck5101.html'
    browser.get(url)
    print('开始进程')
    input1 = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div > div > div > input#username')))  # 获取输入框
    input2 = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div > div > div > input#password')))  # 获取输入框
    input3 = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div > div > div > input#ac_id'))
    )
    submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.m > button')))  # 获取确定按钮
    input1.clear()  # 清空输入框的内容
    input2.clear()  # 清空输入框的内容
    input3.clear()
    input1.send_keys(user)
    input2.send_keys(password)
    input3.send_keys(1)
    submit.click()  # 确定跳转
    html = browser.page_source
    print(html)


index_page(201516070106, 'hu1997')