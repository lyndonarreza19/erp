from django.shortcuts import render


def hello_views(request):
    return render(request, 'inventory/hello.html')
