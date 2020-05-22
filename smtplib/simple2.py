#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 11:54
# @Author  : 一叶知秋
# @File    : simple2.py
# @Software: PyCharm
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

HOST = "smtp.163.com"
SUBJECT = "官网流量数据报表"
TO = "test@qq.com"
FROM = "test@163.com"

msg = MIMEText("""
    <table width="800" border="0" cellspacing="0" cellpadding="4">
      <tr>
        <td bgcolor="#CECFAD" height="20" style="font-size:14px">*官网数据  <a href="monitor.domain.com">更多>></a></td>
      </tr>
      <tr>
        <td bgcolor="#EFEBDE" height="100" style="font-size:13px">
        1）日访问量:<font color=red>152433</font>  访问次数:23651 页面浏览量:45123 点击数:545122  数据流量:504Mb<br>
        2）状态码信息<br>
        &nbsp;&nbsp;500:105  404:3264  503:214<br>
        3）访客浏览器信息<br>
        &nbsp;&nbsp;IE:50%  firefox:10% chrome:30% other:10%<br>
        4）页面信息<br>
        &nbsp;&nbsp;/index.php 42153<br>
        &nbsp;&nbsp;/view.php 21451<br>
        &nbsp;&nbsp;/login.php 5112<br>
	</td>
      </tr>
    </table>""", "html", "utf-8")
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
