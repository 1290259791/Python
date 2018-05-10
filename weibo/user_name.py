from selenium import webdriver


options = webdriver.ChromeOptions()
#   使用 headless 无界面浏览器模式
options.add_argument('--headless')
options.add_argument('--disable-gpu')
#   打开浏览器
driver = webdriver.Chrome(chrome_options=options)

driver.get('http://bj.58.com/jiajiao/pn1')

title = driver.title
print(title)

driver.close()