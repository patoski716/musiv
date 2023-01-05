# Create your views here.
from django.shortcuts import render
# imported our models

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from . models import *

def biography(request,pk):
    bio=Artist.objects.get(id=pk)
    context={'bio':bio}
    return render(request,'artist.html',context)


def index(request):
    post=Song.objects.all()
    #pagination
    songpaginator = Paginator(post, 1)
    songpage = request.GET.get('page')
    songusers = songpaginator.get_page(songpage)
    context={"post":songusers}
    return render(request,"index.html",context)

