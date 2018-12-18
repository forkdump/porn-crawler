import base64
import re
from multiprocessing import Pool
import sqlite3
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver


SEARCH_NUMBER = 3

OPTIONS = webdriver.ChromeOptions()
OPTIONS.headless = True
# INFO = 0, WARNING = 1, LOG_ERROR = 2, LOG_FATAL = 3.0
OPTIONS.add_argument('log-level=3') # hide messages


def get_avgle(query=None):
    if query:
        res = requests.get(
            f"https://api.avgle.com/v1/search/{query}/0?limit={SEARCH_NUMBER}")
        res = res.json()
        title_and_url = []
        for video in res["response"]["videos"]:
            title = video["title"]
            url = video["embedded_url"]
            title_and_url.append((title, url))
    else:
        res = requests.get(f"https://avgle.io/search/%F0%9F%98%8D/1")
        soup = BeautifulSoup(res.text, "lxml")
        a_tags = soup.select("a.single-line")
        title_and_url = []
        for a_tag in a_tags[:SEARCH_NUMBER]:
            res = requests.get(a_tag["href"].replace("avgle.io", "avgle.com"))
            soup = BeautifulSoup(res.text, "lxml")
            title = soup.select_one("title").text
            url = soup.select_one("iframe")["src"]
            title_and_url.append((title, url))
    return title_and_url


def get_youporn(query=None):
    if query:
        res = requests.get(f"https://www.youporn.com/search/?query={query}")
    else:
        res = requests.get("https://www.youporn.com")
    soup = BeautifulSoup(res.text, "lxml")
    a_tags = soup.select("a.video-box-image")
    title_and_url = []
    for a_tag in a_tags[:SEARCH_NUMBER]:
        res = requests.get(f"https://www.youporn.com{a_tag['href']}")
        soup = BeautifulSoup(res.text, "lxml")
        title = soup.select_one("h1.heading2").text
        meta_tag = soup.select_one("meta[name='twitter:player:stream']")
        url = meta_tag["content"].replace("amp;", "")
        title_and_url.append((title, url))
    return title_and_url


def get_pornhub(query=None):
    if query:
        res = requests.get(
            f"https://www.pornhub.com/video/search?search={query}")
    else:
        res = requests.get("https://www.pornhub.com")
    soup = BeautifulSoup(res.text, "lxml")
    a_tags = soup.select("span.title a[href^=/view_video.php?viewkey=]")[4:]
    title_and_url = []
    for a_tag in a_tags[:SEARCH_NUMBER]:
        res = requests.get(f"https://www.pornhub.com{a_tag['href']}")
        soup = BeautifulSoup(res.text, "lxml")
        title = soup.select_one("span.inlineFree").text
        script_tag = soup.select("script[type=text/javascript]")[2]
        url = re.search(
            r'"quality":"\d{3}","videoUrl":"(.*?)"', script_tag.text).group(1)
        url = url.replace("\\", "")
        title_and_url.append((title, url))
    return title_and_url


def get_tube85(query=None):
    if query:
        res = requests.get(f"https://www.85tube.com/search/{query}/")
    else:
        res = requests.get("https://www.85tube.com")
    soup = BeautifulSoup(res.text, "lxml")
    a_tags = soup.select("div.item a")
    title_and_url = []
    for a_tag in a_tags[:SEARCH_NUMBER]:
        res = requests.get(a_tag['href'])
        soup = BeautifulSoup(res.text, "lxml")
        title = soup.select_one("h1").text
        url = soup.select_one("a[data-attach-session]")['href']
        title_and_url.append((title, url))
    return title_and_url


def get_redtube(query=None):
    if query:
        res = requests.get(f"https://www.redtube.com/?search={query}")
    else:
        res = requests.get("https://www.redtube.com")
    soup = BeautifulSoup(res.text, "lxml")
    a_tags = soup.select("div.video_title a")
    title_and_url = []
    for a_tag in a_tags[:SEARCH_NUMBER]:
        res = requests.get(f"https://www.redtube.com{a_tag['href']}")
        soup = BeautifulSoup(res.text, "lxml")
        title = soup.select_one("h1.video_title_text").text
        script_tag = soup.select("script")[12]
        url = re.search(
            r'"quality":"\d{3}","videoUrl":"(.*?)"', script_tag.text).group(1)
        url = url.replace("\\", "")
        title_and_url.append((title, url))
    return title_and_url


def get_popjav(query=None):
    if query:
        res = requests.get(f"https://popjav.tv/?s={query}")
    else:
        res = requests.get("https://popjav.tv")
    soup = BeautifulSoup(res.text, "lxml")
    a_tags = soup.select("a.thumb")
    driver = webdriver.Chrome("./chromedriver.exe", options=OPTIONS)
    title_and_url = []
    for a_tag in a_tags[:SEARCH_NUMBER]:
        res = requests.get(a_tag["href"])
        soup = BeautifulSoup(res.text, "lxml")
        title = soup.select_one("h1.post_title").text
        id_ = soup.select_one("#b_openload")["onclick"]
        id_ = id_.split("'")[1]
        embeded_url = base64.b64decode(id_).decode("utf-8")
        driver.get(embeded_url)
        soup = BeautifulSoup(driver.page_source, "lxml")
        key = soup.select_one("#DtsBlkVFQx").text
        url = f"https://openload.co/stream/{key}"
        url = requests.get(url, allow_redirects=False).headers["location"]
        title_and_url.append((title, url))
    driver.quit()
    return title_and_url


def get_thisav(query=None):
    if query:
        res = requests.get(f"https://www.thisav.com/channel/{query}")
    else:
        res = requests.get("https://www.thisav.com")
    soup = BeautifulSoup(res.text, "lxml")
    a_tags = soup.select("div.video_box a")
    title_and_url = []
    for a_tag in a_tags[:SEARCH_NUMBER]:
        res = requests.get(a_tag['href'])
        res.encoding = "utf-8"
        soup = BeautifulSoup(res.text, "lxml")
        title = soup.select_one("div.span-640.left h1").text
        url = soup.select_one("iframe")["src"]
        title_and_url.append((title, url))
    return title_and_url


def get_xvideos(query=None):
    if query:
        res = requests.get(f"https://www.xvideos.com/?k={query}")
    else:
        res = requests.get("https://www.xvideos.com")
    soup = BeautifulSoup(res.text, "lxml")
    a_tags = soup.select("p a[title]")
    title_and_url = []
    for a_tag in a_tags[:SEARCH_NUMBER]:
        title = a_tag.text
        id_ = a_tag["href"].split("/")[1][5:]
        url = f"https://www.xvideos.com/embedframe/{id_}"
        title_and_url.append((title, url))
    return title_and_url


FUNCS = (get_avgle, get_youporn, get_pornhub, get_tube85,
         get_redtube, get_popjav, get_thisav, get_xvideos)
SITES = ("Avgle", "Youporn", "Pornhub", "Tube85",
         "Redtube", "Popjav", "Thisav", "Xvideos")

if __name__ == "__main__":
    con = sqlite3.connect("./website/db.sqlite3")
    cur = con.cursor()
    
    while True:
        cur.execute("select keyword from Query")
        try:
            query = cur.fetchone() # None
        except:
            query = cur.fetchone()[0] # (query,)[0]

        minute = time.localtime(time.time())[4]
        second = time.localtime(time.time())[5]
        every_five_minute = not(minute % 5) and second == 0

        if query or every_five_minute:
            if query:
                print("\nDon't interrupt during searching.\n")
            else:
                print("\nDon't interrupt during the update.\n")

            with Pool() as pool:
                results = [pool.apply_async(func, (query,)) for func in FUNCS]  # crawled with multiprocessing
                for site, result in zip(SITES, results):
                    cur.execute(f"delete from {site}{'Query' if query else ''}") # delete from "site" or "siteQuery"
                    con.commit()
                    try:
                        data = result.get(timeout=10)
                        print(f"{site}...ok")
                    except:
                        data = [("no result", "https://via.placeholder.com/500?text=no+result") for i in range(3)]
                        print(f"{site}...got some problems.")
                    cur.executemany(f"insert into {site}{'Query' if query else ''} values (null,?,?)", data)  # id = null
                    con.commit()
                cur.execute("delete from Query")
                con.commit()

            print("\nDone\n")
