from django.shortcuts import render
import datetime


def index(request):
    todays_date = datetime.date.today()
    return render(request, "index/index.html", {
        "todays_date": todays_date
    })
