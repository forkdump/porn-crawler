from django.shortcuts import render
from crawler.models import *

# Create your views here.
def index(request):
    if "query" in request.GET:
        query.objects.create(id=None, keyword=request.GET["query"])
        while True: # wait until crawl done
            if not query.objects.all():
                return render(request, 'index.html', {"videos": videos_after_searched.objects.all()})
    else:
        return render(request, 'index.html', {"videos": videos.objects.all()})