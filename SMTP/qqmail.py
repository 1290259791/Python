import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import chong
import reptile
my_sender = '1290259791@qq.com'
my_pass = 'qmvrshslxuojjeii'


def mail(receivers, content):
    ret = True
    try:
        msg = MIMEText(content, 'html', 'utf-8')
        msg['From'] = formataddr(["FromRunoob", my_sender])  # 发件人昵称,账户
        msg['To'] = formataddr(["FK", receivers])  # 收件人的昵称和账户
        msg['Subject'] = '邮件主题'  # 邮件的主题
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱SMTP服务器端口
        server.login(my_sender, my_pass)  # 发件人的账户,密码
        server.sendmail(my_sender, [receivers, ], msg.as_string())
        server.quit()
    except Exception as e:
        print(e)
        ret = False

    return ret


my_user = '1290259791@qq.com'
# content = '文件的内容'
# gethtml = chong.gethtml()
gethtml = reptile.gettext()
print(gethtml)
texts = ""
# 如有乐享
# for url, name in gethtml:
#     text = "<p><a href=\""+url+"\">"+name+"</a></p>"
#     texts += text

# 拔羊毛
for url, day, time, name in gethtml:
    text = "<p><a href=\"http://www.8ym.cn" + url + "\">" + name + "</a></p>"
    texts += text
ret = mail(my_user, texts)
print(ret)
