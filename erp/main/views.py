from django.shortcuts import render


def about(request):
    return render(request, 'main/about.html')

def index(request):
    return render(request,'base.html')

