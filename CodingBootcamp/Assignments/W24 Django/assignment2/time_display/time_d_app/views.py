from django.shortcuts import render, redirect
from time import gmtime,strftime
# from datetime import datetime
# import pytz

# Create your views here.
def index(request):
    return redirect('/time_display')

def time(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, 'index.html',context)