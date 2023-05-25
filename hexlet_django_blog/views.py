from django.shortcuts import render

def index(request):
    return render(request, 'article/index.html', context={
        'app_name': 'Articles',
    })


def about(request):
    return render(request, 'about.html')
