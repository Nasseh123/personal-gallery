from django.shortcuts import render
from .models import image
# Create your views here.
def index(request):
    imaged=image.allimages()
    return render(request,'index.html',{"imaged":imaged,})