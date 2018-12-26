from django.shortcuts import render
import sqlite3
from crawler.crawler import SITES

# Create your views here.
def index(request):
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    sql = "select * from {}"

    if "query" in request.GET:
        sql = "select * from {}_query"
        cur.execute(f"insert into query values (?)", (request.GET["query"],)) # insert keyword into query table
        con.commit()
        while True: # wait until crawl done
            cur.execute("select keyword from query")
            if not cur.fetchone():
                break

    all_videos = []
    for site in SITES:
        cur.execute(sql.format(site))
        table = cur.fetchall()
        if not table:
            continue

        videos = []
        for row in table:
            videos.append({"title": row[0], "url": row[1], "logo": row[2]})
        if videos:
            all_videos.append(videos)    
    con.close()
    return render(request, 'index.html', {"all_videos": all_videos}) # all_videos = [ [{}{}{}...] ... ]