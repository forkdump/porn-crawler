from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    # View code here...
    return render(request, 'index.html', {
        "all_videos": (
            Avgle.objects.all(),
            Youporn.objects.all(),
            Pornhub.objects.all(),
            Tube85.objects.all(),
            Redtube.objects.all(),
            Popjav.objects.all(),
            Thisav.objects.all(),
            Xvideos.objects.all()
        )})
