from django.shortcuts import render
from crawler.models import *

# Create your views here.
def index(request):
    if "query" in request.GET:
        # insert keyword into Query table
        Query.objects.create(keyword=request.GET["query"])
        while True:
            try:
                Query.objects.get() # wait until crawl done
            except:
                all_videos = []
                globals_ = globals()
                for table in globals_:
                    if table.endswith("Query") and globals_[table]:
                        all_videos.append(globals_[table].objects.all())
                return render(request, 'index.html', {"all_videos": all_videos})
    else:
        all_videos = []
        globals_ = globals()
        for table in globals_:
            if table.endswith("Query") and globals_[table]:
                all_videos.append(globals_[table].objects.all())
        return render(request, 'index.html', {"all_videos": all_videos})
