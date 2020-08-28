#!/usr/bin/env python3

import requests
import re
from six.moves.urllib.parse import urlparse

target_url = "http://192.168.1.86/mutillidae/"
target_links = []


def extract_links_from(url):
    response = requests.get(target_url)
    return re.findall('(?:href=")(.*?)"', response.content.decode())


def crawl(url):
    href_links = extract_links_from(url)
    for link in href_links:
        link = urlparse.par(url, link)

        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)


crawl(target_url)
