from django.shortcuts import render
from datetime import datetime

# Create your views here.


def index(request, tvno=0):
    tv_list = [
        {'name': '中天',  'tvcode': 'wUPPkSANpyo'},
        {'name': '民視',  'tvcode': 'XxJKnDLYZz4'},
    ]
    now = datetime.now()
    tvno = tvno
    tv = tv_list[tvno]

    return render(request, 'tvshow.html', locals())
