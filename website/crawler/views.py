from django.shortcuts import render
import sqlite3
from crawler.crawler import SITES

# Create your views here.
def index(request):
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    for site in SITES:
        cur.execute(f"select * from {site}_query")
        cur.fetchall()
        
    if "query" in request.GET:
        # insert keyword into Query table
        # Query.objects.create(keyword=request.GET["query"])
        while True:
            try:
                Query.objects.get() # wait until crawl done
            except:
                all_videos = []
                globals_ = globals()
                for table in globals_:
                    if table.endswith("query") and globals_[table]:
                        all_videos.append(globals_[table].objects.all())
                return render(request, 'index.html', {"all_videos": all_videos})
    else:
        all_videos = []
        globals_ = globals()
        for table in globals_:
            if table.endswith("query") and globals_[table]:
                all_videos.append(globals_[table].objects.all())
        return render(request, 'index.html', {"all_videos": all_videos})
