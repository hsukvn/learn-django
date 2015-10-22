from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    excuses = [
        "It was working in my head",
        "I thought I fixed that",
        "Actually, that is a feature",
        "It works on my machine",
    ]

    rand_excuse=random.choice(excuses)

    return render(request, "copyleft.html", {'excuse': rand_excuse})

    return HttpResponse(output)
