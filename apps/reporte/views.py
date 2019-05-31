from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

from apps.reporte.forms import ReporteForm
from apps.reporte.models import Reporte


def index_reporte(request):
    return render(request, 'reporte/index.html')

def reporte_view(request):
	if request.method=='POST':
		form=ReporteForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('reporte:index')
	else:
		form=ReporteForm()
	return render(request,'reporte/reporte_form.html',{'form': form})


def reporte_list(request):
	reporte = Reporte.objects.all()
	contexto= {'reporte': reporte}
	return render(request, 'reporte/reporte_list.html', contexto)

def reporte_edit(request, id_reporte):
	reporte = Reporte.objects.get(id=id_reporte)
	if request.method == 'GET':
		form = ReporteForm(instance=reporte)
	else:
		form = ReporteForm(request.POST, instance=reporte)
		if form.is_valid():
			form.save()
		return redirect('reporte:reporte_listar')
	return render(request, 'reporte/reporte_form.html', {'form':form})

def reporte_delete(request, id_reporte):
	reporte = Reporte.objects.get(id=id_reporte)
	if request.method == 'POST':
		reporte.delete()
		return redirect('reporte:reporte_listar')
	return render(request, 'reporte/reporte_delete.html', {'reporte':reporte})