"""This is the landing page navbar view"""
from datetime import date
from django.shortcuts import render, redirect


def index(request):
    """Show todays date in the navbar"""
    todays_date = date.today()
    # If the user is already authenticated, then redirect them back to the main dashboard
    if request.user:
        return redirect("todo")

    return render(request, "index/index.html", {
        "todays_date": todays_date
    })
