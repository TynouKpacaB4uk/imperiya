from django.shortcuts import render

def games(request):
    return render(request,'games/games.html', locals())
