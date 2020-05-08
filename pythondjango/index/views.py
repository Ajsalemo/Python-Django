"""This is the landing page navbar view"""
from datetime import date
from django.shortcuts import render


def index(request):
    """Show todays date in the navbar"""
    todays_date = date.today()
    return render(request, "index/index.html", {
        "todays_date": todays_date
    })
