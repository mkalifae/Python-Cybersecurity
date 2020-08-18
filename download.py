#!/usr/env python
import requests

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

download("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/2020-nissan-gt-r-nismo-101-1563221484.jpg")