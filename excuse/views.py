from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    excuses = [
        "It was working in my head",
        "I thought I fixed that",
        "Actually, that is a feature",
        "It works on my machine",
    ]

    output = ''
    for excuse in excuses:
        output += excuse + '<br>'

    return HttpResponse(output)
