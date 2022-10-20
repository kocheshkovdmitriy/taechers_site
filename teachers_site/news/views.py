from django.shortcuts import render
from .models import New

def new_list(request):
    news = New.objects.all()
    return render(request, "news/news_list.html", {'news': news})