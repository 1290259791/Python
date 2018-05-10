from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq


options = webdriver.ChromeOptions()
#   使用 headless 无界面浏览器模式
options.add_argument('--headless')
options.add_argument('--disable-gpu')
#   打开浏览器
browser = webdriver.Chrome(chrome_options=options)
wait = WebDriverWait(browser, 10)  # 显示加载
KEYWORD = 'iPad'
file = open('iPad.txt', 'w')

def index_page(page):
    """
    抓取索引页
    :param page:
    :return:
    """
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))  # 获取输入框
            submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > '
                                                                                 'span.btn.J_Submit')))  # 获取确定按钮
            input.clear()  # 清空输入框的内容
            input.send_keys(page)  # 填入页码
            submit.click()  # 确定跳转
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page))
        )  # 确定当前页码亮
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item'))
        )  # 判断页面商品信息
        get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    """
    提取商品数据
    :return:
    """
    print('提取商品')
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        file.write(product.__str__() + '\n')


MAX_PAGE = 10


def main():
    """
    遍历每页
    :return:
    """
    for i in range(MAX_PAGE):
        index_page(i+1)
    file.close()


if __name__ == '__main__':
    main()
