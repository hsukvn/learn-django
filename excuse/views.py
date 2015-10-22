from django.shortcuts import render
from excuse.models import Excuse
import random

# Create your views here.

def home(request):
    rand_excuse=random.choice(Excuse.objects.all())
    return render(request, "copyleft.html", {'excuse': rand_excuse.content})
