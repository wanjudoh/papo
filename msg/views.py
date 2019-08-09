from django.shortcuts import render, get_object_or_404, redirect
from .models import Msg

# Create your views here.
def link(request):
    return render(request, 'link.html')

def coloring(request):
    colorings = Msg.objects.filter(group="color")
    return render(request, 'coloring.html',{'colorings':colorings})

def icon(request):
    icons = Msg.objects.filter(group="img")
    return render(request, 'icon.html',{'icons':icons})

def abroad(request):
    abroads = Msg.objects.filter(group="template")
    return render(request, 'abroad.html',{'abroads':abroads})

def font(request):
    fonts = Msg.objects.filter(group="font")
    return render(request, 'font.html',{'fonts':fonts})
