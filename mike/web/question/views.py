from django.shortcuts import render

def question(request):
    return render(request,'question/question.html', locals())

