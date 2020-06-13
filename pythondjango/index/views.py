"""This is the landing page navbar view"""
from django.shortcuts import render, redirect


def index(request):
    """Homepage view"""
    # If the user is already authenticated, then redirect them back to the main dashboard
    if request.user.is_authenticated:
        return redirect("todo")

    return render(request, "index/index.html")


def handler404(request, exception):
    """Display a custom 404"""
    return render(request, "index/404.html", {
        "exception": exception
    })


def handler500(request, exception):
    """Display a custom 500"""
    return render(request, "index/500.html", {
        "exception": exception
    })


def handler502(request, exception):
    """Display a custom 502"""
    return render(request, "index/502.html", {
        "exception": exception
    })


def handler503(request, exception):
    """Display a custom 503"""
    return render(request, "index/503.html", {
        "exception": exception
    })
    