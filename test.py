# av pop this tube
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


res = requests.get(
            f"https://api.avgle.com/v1/search/三上/0?limit=3")
res = res.json()
title_and_url = []
for video in res["response"]["videos"]:
    title = video["title"]
    url = video["embedded_url"]
    title_and_url.append((title, url))
print(title_and_url)