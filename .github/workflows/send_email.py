import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
import time

# 发件人邮箱账户
my_sender = 'jsyfzx@hezongyy.com'
# 邮箱口令
mail_pass = 'yP9pXhsBhJQJYhSb'
smtp_host = 'smtp.exmail.qq.com'
smtp_port = 465


def send_email_to(receivers, _topic, mail_contents):
    ret = True

    try:
        message = MIMEText(mail_contents, 'plain', 'utf-8')
        message['From'] = formataddr(['Github Action', my_sender])
        message['To'] = Header(receivers, 'utf-8')

        message['Subject'] = _topic

        server = smtplib.SMTP_SSL(smtp_host, smtp_port)
        server.login(my_sender, mail_pass)
        server.sendmail(my_sender, receivers, message.as_string())
        server.quit()
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ":邮件发送成功")
    except smtplib.SMTPException:
        ret = False
        print("邮件发送失败")
    return ret, time.time()


receiver = "dunett@163.com"
topic = "[docker-pull]Images pushed to Aliyun succeed"
content = 'test'

image_tags = open('to_pull.txt').readlines()
images = ['images pushed to Aliyun Registry:']
image_prefix = "registry.cn-chengdu.aliyuncs.com/mirror_d"
for tag in image_tags:
    tag = tag.strip()
    if len(tag) == 0 or tag.startswith('#'):
        continue
    source_tag = tag.split(' ')[0]
    target_tag = tag.split(' ')[1]
    images.append(f"{source_tag} -> {image_prefix}/{target_tag}-arm64")
    images.append(f"{source_tag} -> {image_prefix}/{target_tag}-amd64")

send_email_to(receiver, topic, "\n\n".join(images))
