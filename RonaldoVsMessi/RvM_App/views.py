from django.shortcuts import render
from .models import Ronaldo,Messi

# Create your views here.
def index(request):
    ronaldo_score = Ronaldo.objects.first().score_r
    messi_score = Messi.objects.first().score_m
    return render(request, 'RvM_App/index.html', {
        'score_m': messi_score,
        'score_r': ronaldo_score
    })
