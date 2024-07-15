from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.order_by('data').filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.filter(publicada=True)
    if "buscar" in request.GET:
        query = request.GET["buscar"]
        if query:
            fotografias = fotografias.filter(nome__icontains=query)
    return render(request, 'galeria/buscar.html', {"cards": fotografias})