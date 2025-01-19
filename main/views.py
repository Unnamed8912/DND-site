from django.http import HttpResponse
from django.shortcuts import render

def characters(request):
    context = {
        'title' : 'Персонажи',
    }
    return render(request, 'main/characters.html', context)

def fight(request):
    return render(request, 'main/fight.html')

def notes(request):
    return render(request, 'main/notes.html')

def history(request):
    return render(request, 'main/history.html')