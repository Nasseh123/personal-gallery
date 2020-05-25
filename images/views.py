from django.shortcuts import render
from .models import image,category,location
from django.http import HttpResponse,Http404 #RESPONSIBLE FOR RETURNING A RESPONSE TO A USER
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
categorys=category.allcategory()
locations=location.alllocation()
imaged=image.allimages()

def index(request):
    # print(categorys)
    return render(request,'index.html',{"imaged":imaged,'category':categorys,'location':locations})

def search_results(request):
    if 'image_name' in request.GET and request.GET['image_name']:
        search_name=request.GET.get('image_name')
        searched_image=image.search_by_name(search_name)
        message = f"{search_name}"

        return render(request, 'search.html',{"message":message,"images": searched_image,"imaged":imaged,'category':categorys,'location':locations})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


def imagepath(request,image_id):
    try:
        imageds= image.objects.get(id = image_id)
        print(imageds)
    except DoesNotExist:
        raise Http404()
    return render(request,"image.html", {"imageds":imageds,'category':categorys,'location':locations})


def categorie(request,category_id,context=None):
    
        categoriey=category.objects.get(id=category_id)
        imagedsd=image.objects.get(category=categoriey)
        print(categoriey)
        
        return render(request,"category.html",{"categoriey":categoriey,"imaged":imaged,'category':categorys})

def categorie(request,category_id,context=None):
    
        categoriey=category.objects.get(id=category_id)
        imagedsd=image.objects.get(category=categoriey)
        print(categoriey)
        
        return render(request,"category.html",{"categoriey":categoriey,"imaged":imaged,'category':categorys,'location':locations})