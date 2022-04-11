#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 12:00
# @Author  : 一叶知秋
# @File    : simple4.py
# @Software: PyCharm
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import formatdate
from email.mime.application import MIMEApplication

HOST = "smtp.163.com"
SUBJECT = "官网业务服务质量周报"
TO = "test@qq.com"
FROM = "test@163.com"


def addimg(src, imgid):
    with open(src, 'rb') as fp:
        msgImage = MIMEImage(fp.read())
    msgImage.add_header('Content-ID', imgid)
    return msgImage


msg = MIMEMultipart('related')
msgtext = MIMEText("<font color=red>官网业务周平均延时图表:<br><img src=\"cid:weekly\" border=\"1\"><br>详细内容见附件。</font>", "html",
                   "utf-8")
msg.attach(msgtext)
msg.attach(addimg("img/weekly.png", "weekly"))

attach = MIMEApplication(open("doc/week_report.xlsx", "rb").read())
attach.add_header('Content-Disposition', 'attachment', filename="week_report.xlsx")
msg.attach(attach)

msg['Subject'] = SUBJECT
msg['From'] = FROM
msg['To'] = TO
msg['Date'] = formatdate()


def main():
    try:
        server = smtplib.SMTP()
        server.connect(HOST, 25)
        server.login(FROM, "123456")
        server.set_debuglevel(1)  # 打印出和SMTP服务器交互的所有信息。
        server.sendmail(FROM, TO, msg.as_string())
        server.quit()
        print("邮件发送成功！")
    except Exception as e:
        print(f"失败：{str(e)}")


if __name__ == '__main__':
    main()
