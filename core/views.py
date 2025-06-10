from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse('THis is my first function')

def home_view(request):
    context = {
        'name': 'Simmi',
        'title': 'Django Learning',
    }
    return render(request, 'home.html', context)
