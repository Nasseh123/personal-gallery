from django.shortcuts import render
from .models import image,category,location
from django.http import HttpResponse,Http404 #RESPONSIBLE FOR RETURNING A RESPONSE TO A USER
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
categorys=category.allcategory()
locations=location.alllocation()
def index(request):
    imaged=image.allimages()
    print(imaged)
    
    # print(categorys)
    return render(request,'index.html',{"imaged":imaged,'category':categorys,'location':locations})

def search_results(request):
    if 'image_name' in request.GET and request.GET['image_name']:
        search_name=request.GET.get('image_name')
        searched_image=image.search_by_name(search_name)
        message = f"{search_name}"

        return render(request, 'search.html',{"message":message,"images": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


def imagepath(request,image_id):
    try:
        imageds= image.objects.get(id = image_id)
        print(imageds)
    except DoesNotExist:
        raise Http404()
    return render(request,"image.html", {"imageds":imageds})