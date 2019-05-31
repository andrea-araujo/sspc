from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

from apps.herramienta.forms import HerramientaForm
from apps.herramienta.models import Herramienta


def index_herramientas(request):
    return render(request, 'herramienta/index.html')

def herramienta_view(request):
	if request.method == 'POST':
		form=HerramientaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('herramienta:indexHerramienta')
	else:
		form= HerramientaForm()
	return render(request, 'herramienta/herramienta_form.html', {'form': form })


def herramienta_list(request):
	herramienta = Herramienta.objects.all()
	contexto= {'herramienta': herramienta}
	return render(request, 'herramienta/herramienta_list.html', contexto)

def herramienta_edit(request, id_herramienta):
	herramienta = Herramienta.objects.get(id=id_herramienta)
	if request.method == 'GET':
		form = HerramientaForm(instance=herramienta)
	else:
		form = HerramientaForm(request.POST, instance=herramienta)
		if form.is_valid():
			form.save()
		return redirect('herramienta:herramienta_listar')
	return render(request, 'herramienta/herramienta_form.html', {'form':form})

def herramienta_delete(request, id_herramienta):
	herramienta = Herramienta.objects.get(id=id_herramienta)
	if request.method == 'POST':
		herramienta.delete()
		return redirect('herramienta:herramienta_listar')
	return render(request, 'herramienta/herramienta_delete.html', {'herramienta':herramienta})