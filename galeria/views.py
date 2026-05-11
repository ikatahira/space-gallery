# galeria/views.py — recebe o foto_id
from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})