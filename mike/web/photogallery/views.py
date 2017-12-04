from django.shortcuts import render

def photogallery(request):
    return render(request,'photogallery/photogallery.html', locals())


