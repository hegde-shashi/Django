from django.shortcuts import render
from .models import world

def test(request):
    tours = world.objects.all()
    context = { "tours": tours }
    return render(request, "tour/index.html", context)

def stat(request):
    return render(request, "page/index.html")

# Create your views here.
