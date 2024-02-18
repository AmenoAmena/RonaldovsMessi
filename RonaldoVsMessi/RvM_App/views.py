from django.shortcuts import render
from .models import Ronaldo, Messi

def index(request):
    ronaldo_instance, created_r = Ronaldo.objects.get_or_create(pk=1)
    ronaldo_score = ronaldo_instance.score_r

    messi_instance, created_m = Messi.objects.get_or_create(pk=1)
    messi_score = messi_instance.score_m

    if request.method == 'POST':
        player = request.POST.get('player')
        if player == 'ronaldo':
            ronaldo_instance.increase_score_r()
        elif player == 'messi':
            messi_instance.increase_score_m()

    return render(request, 'RvM_App/index.html', {
        'score_m': messi_score,
        'score_r': ronaldo_score
    })

