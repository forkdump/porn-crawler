# import requests
# from bs4 import BeautifulSoup

# res = requests.get(f"https://www.thisav.com/channel/三上")

# res = requests.get("https://www.thisav.com")
# soup = BeautifulSoup(res.text, "lxml")
# a_tags = soup.select("div.video_box a")
# title_and_url = []
# for a_tag in a_tags[:3]:
#     res = requests.get(a_tag['href'])
#     res.encoding = "utf-8"
#     soup = BeautifulSoup(res.text, "lxml")
#     title = soup.select_one("div.span-640.left h1").text
#     url = soup.select_one("iframe")["src"]
#     title_and_url.append((title, url))