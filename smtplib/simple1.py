#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 11:53
# @Author  : 一叶知秋
# @File    : simple1.py
# @Software: PyCharm
import smtplib

HOST = "smtp.163.com"
SUBJECT = "Test email from Python"
TO = "test@qq.com"
FROM = "test@163.com"
text = "Python rules them all!"
BODY = "\r\n".join(
    (f"From: {FROM}", f"To: {TO}", f"Subject: {SUBJECT}", "", text)
)


def main():
    try:
        server = smtplib.SMTP()
        server.connect(HOST, 25)
        server.login(FROM, "123456")
        server.set_debuglevel(1)
        server.sendmail(FROM, [TO], BODY)
        server.quit()
        print("邮件发送成功！")
    except Exception as e:
        print(f"失败：{str(e)}")


if __name__ == '__main__':
    main()
