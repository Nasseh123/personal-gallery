from django.shortcuts import render
from .models import image
# Create your views here.
def index(request):
    imaged=image.allimages()
    return render(request,'index.html',{"imaged":imaged,})

def search_results(request):
    if 'image_name' in request.GET and request.GET['image_name']:
        search_name=request.GET.get('image_name')
        searched_image=image.search_by_name(search_name)
        message = f"{search_name}"

        return render(request, 'search.html',{"message":message,"images": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})