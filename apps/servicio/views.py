from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from apps.servicio.forms import ServicioForm
from apps.servicio.models import Servicio


def index_servicio(request):
	return render(request, 'servicio/index.html')

def servicio_view(request):
	if request.method == 'POST':
		form = ServicioForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('servicio:indexServicio')
	else:
		form = ServicioForm()

	return render(request, 'servicio/servicio_form.html', {'form':form})

def servicio_list(request):
	servicio = Servicio.objects.all()
	contexto= {'servicio': servicio}
	return render(request, 'servicio/servicio_list.html', contexto)

def servicio_edit(request, id_servicio):
	servicio = Servicio.objects.get(id=id_servicio)
	if request.method == 'GET':
		form = ServicioForm(instance=servicio)
	else:
		form = ServicioForm(request.POST, instance=servicio)
		if form.is_valid():
			form.save()
		return redirect('servicio:servicio_listar')
	return render(request, 'servicio/servicio_form.html', {'form':form})

def servicio_delete(request, id_servicio):
	servicio = Servicio.objects.get(id=id_servicio)
	if request.method == 'POST':
		servicio.delete()
		return redirect('servicio:servicio_listar')
	return render(request, 'servicio/servicio_delete.html', {'servicio':servicio})