#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 11:55
# @Author  : 一叶知秋
# @File    : simple3.py
# @Software: PyCharm
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import formatdate

HOST = "smtp.163.com"
SUBJECT = "业务性能数据报表"
TO = "test@qq.com"
FROM = "test@163.com"


def addimg(src, imgid):
    fp = open(src, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', imgid)
    return msgImage


msg = MIMEMultipart('related')
msgtext = MIMEText("""
<table width="600" border="0" cellspacing="0" cellpadding="4">
      <tr bgcolor="#CECFAD" height="20" style="font-size:14px">
        <td colspan=2>*官网性能数据  <a href="monitor.domain.com">更多>></a></td>
      </tr>
      <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
        <td>
         <img src="cid:io"></td><td>
         <img src="cid:key_hit"></td>
      </tr>
      <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
         <td>
         <img src="cid:men"></td><td>
         <img src="cid:swap"></td>
      </tr>
    </table>""", "html", "utf-8")
msg.attach(msgtext)
msg.attach(addimg("img/bytes_io.png", "io"))
msg.attach(addimg("img/myisam_key_hit.png", "key_hit"))
msg.attach(addimg("img/os_mem.png", "men"))
msg.attach(addimg("img/os_swap.png", "swap"))

msg['Subject'] = SUBJECT
msg['From'] = FROM
msg['To'] = TO
msg['Date'] = formatdate()


def main():
    try:
        server = smtplib.SMTP()
        server.connect(HOST, 25)
        server.login(FROM, "123456")
        server.sendmail(FROM, TO, msg.as_string())
        server.quit()
        print("邮件发送成功！")
    except Exception as e:
        print("失败：" + str(e))


if __name__ == '__main__':
    main()
