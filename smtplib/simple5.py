#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 15:01
# @Author  : 一叶知秋
# @File    : simple5.py
# @Software: PyCharm
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def add_attachment(email_attachment_address, msgRoot):
    # 添加附件
    for path in email_attachment_address:
        if path.endswith(('.jpg', '.png')):
            # jpg
            picture_name = path.split('\\')[-1]
            part = MIMEApplication(open(path, 'rb').read())
            part.add_header('Content-Disposition', 'attachment', filename=picture_name)
            msgRoot.attach(part)

        if path.endswith('.pdf'):
            # pdf
            pdf_name = path.split('\\')[-1]
            part = MIMEApplication(open(path, 'rb').read())
            part.add_header('Content-Disposition', 'attachment', filename=pdf_name)
            msgRoot.attach(part)

        if path.endswith(('.docx', '.pptx', '.xlsx')):
            # doc,xlsx,ppt
            office_name = path.split('\\')[-1]
            part = MIMEApplication(open(path, 'rb').read())
            part.add_header('Content-Disposition', 'attachment', filename=office_name)
            msgRoot.attach(part)

        if path.endswith('.txt'):
            # txt
            txt_name = path.split('\\')[-1]
            part = MIMEApplication(open(path, 'rb').read())
            part.add_header('Content-Disposition', 'attachment', filename=txt_name)
            msgRoot.attach(part)

        if path.endswith('.mp3'):
            # mp3
            mp3_name = path.split('\\')[-1]
            part = MIMEApplication(open(path, 'rb').read())
            part.add_header('Content-Disposition', 'attachment', filename=mp3_name)
            msgRoot.attach(part)

        if path.endswith(('.zip','.tar','.gz')):
            # tar zip tar.gz
            compress_name = path.split('\\')[-1]
            part = MIMEApplication(open(path, 'rb').read())
            part.add_header('Content-Disposition', 'attachment', filename=compress_name)
            msgRoot.attach(part)


def send_email(email_subject, email_content, email_attachment_address, email_receiver):
    sender = 'test@163.com'
    passwd = '123456'
    receivers = email_receiver  # 邮件接收人
    msgRoot = MIMEMultipart()
    msgRoot['Subject'] = email_subject
    msgRoot['From'] = sender
    msgRoot['To'] = ';'.join(receivers) if len(receivers) > 1 else receivers[0]
    part = MIMEText(email_content)
    msgRoot.attach(part)

    # 添加附件
    add_attachment(email_attachment_address, msgRoot)
    server = None
    try:
        server = smtplib.SMTP()
        server.connect('smtp.163.com')
        server.login(sender, passwd)
        server.sendmail(sender, receivers, msgRoot.as_string())
        print('邮件发送成功')
    except smtplib.SMTPException as e:
        print('邮件发送失败')
    finally:
        server.quit()


def main():
    # 发送测试邮件
    email_subject = 'python 邮件测试'
    email_content = 'hello world'
    file_dir = r'C:\Users\liming\Desktop\file_dir'
    email_attachment_address = [os.path.join(file_dir, file) for file in os.listdir(file_dir)]
    email_receiver = ['test1@qq.com', 'test2@qq.com']
    send_email(email_subject, email_content, email_attachment_address, email_receiver)


if __name__ == '__main__':
    main()
