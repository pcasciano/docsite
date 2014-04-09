from django.shortcuts import render


def index(request):
    context = {'title': 'Home doc rest api'}
    return render(request, 'docsite/doc.html', context)
