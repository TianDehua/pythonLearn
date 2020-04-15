fromAddr = 'send@163.com ' #发件地址
password= '' #发件密码

toAddr = 'receive@qq.com' #收件地址
smtpServer = 'smtp@163.com' #smtp 服务器地址， 发送邮件使用 smtp 协议

import smtplib
from email.mime.text import MIMEText

msg = MIMEText('hello, send by Python', 'plain', 'utf-8')
print('msg=', msg)
print('as_string=', msg.as_string)

server = smtplib.SMTP(smtpServer, 25)
server.set_debuglevel(1)
server.login(fromAddr, password)
server.sendmail(fromAddr, [toAddr], msg.as_string)
server.quit()