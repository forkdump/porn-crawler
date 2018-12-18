from django.shortcuts import render
from crawler.models import *

# Create your views here.


def index(request):
    # View code here...
    if "query" in request.GET:
        Query.objects.create(keyword=request.GET["query"]) # insert keyword into Query table
        while True:
            try:
                Query.objects.get() # wait until crawl done
            except:
                return render(request, 'index.html', {"all_videos": (
                    AvgleQuery.objects.all(),
                    YoupornQuery.objects.all(),
                    PornhubQuery.objects.all(),
                    Tube85Query.objects.all(),
                    RedtubeQuery.objects.all(),
                    PopjavQuery.objects.all(),
                    ThisavQuery.objects.all(),
                    XvideosQuery.objects.all()
                )})
    else:
        return render(request, 'index.html', {"all_videos": (
            Avgle.objects.all(),
            Youporn.objects.all(),
            Pornhub.objects.all(),
            Tube85.objects.all(),
            Redtube.objects.all(),
            Popjav.objects.all(),
            Thisav.objects.all(),
            Xvideos.objects.all()
        )})
