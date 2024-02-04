from django.shortcuts import render
from .models import TurModel, Image

def core(request):
    tur = TurModel.objects.all()
    best = TurModel.objects.all()[:3]
    context = {
        "tur": tur,
        "best": best
    }
    return render(request, 'app/core.html', context)

def detail(request, id):
    det = TurModel.objects.get(id=id)
    context = {"det":det}
    return render(request, 'app/detail.html', context)

def about(request):
    return render(request, 'app/about.html  ')

def galerea(request):
    gal = Image.objects.all()
    return render(request, 'app/galerea.html', {'gal':gal})

def galerea_detail(request,id):
    gal_d = Image.objects.get(id=id)
    return render(request, 'app/galerea_detail.html', {"gal_d": gal_d})