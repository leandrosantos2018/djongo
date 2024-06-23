from django.shortcuts import render, get_object_or_404

from galeria.models import fotografia



def index(request):
    fotografias = fotografia.objects.order_by("data_foto").filter(publicada=True)

    return render(request, 'galeria/index.html',{"cards":fotografias})

def imagem(request,foto_id):
    foto = get_object_or_404(fotografia,pk=foto_id)
    return render(request, 'galeria/imagem.html',{"fotografia": foto})


def buscar(request,):
    fotografias = fotografia.objects.order_by("data_foto").filter(publicada=True)
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotos = fotografia.objects.filter(nome__icontains=nome_a_buscar)

    return render(request,"galeria/buscar.html",{"cards":fotos})
