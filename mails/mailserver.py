# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText


class MailServer(object):
    def __init__(self, host, port, username, password, use_ssl=False):
        if use_ssl:
            self.smtp = smtplib.SMTP_SSL()
        else:
            self.smtp = smtplib.SMTP()
        self.host = host
        self.port = int(port)
        self.username = username
        self.password = password

    def sendmail(self, sender, receiver, subject, content):
        message = MIMEText(content, _subtype="html", _charset="utf-8")
        message["Subject"] = subject
        message["From"] = sender
        message["To"] = receiver

        self.smtp.connect(self.host, self.port)
        self.smtp.login(self.username, self.password)
        self.smtp.sendmail(sender, [receiver], message.as_string())
        self.smtp.close()
