from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

from apps.empleado.forms import EmpleadoForm
from apps.empleado.models import Empleado

def index_empleado(request):
    return render(request, 'empleado/index.html')

def empleado_view(request):
	if request.method=='POST':
		form=EmpleadoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('empleado:indexEmpleado')
	else:
		form=EmpleadoForm()
	return render(request,'empleado/empleado_form.html',{'form': form})

def empleado_list(request):
	empleado = Empleado.objects.all().order_by('id')
	contexto= {'empleado': empleado}
	return render(request, 'empleado/empleado_list.html', contexto)

def empleado_edit(request, id_empleado):
	empleado = Empleado.objects.get(id=id_empleado)
	if request.method == 'GET':
		form = EmpleadoForm(instance=empleado)
	else:
		form = EmpleadoForm(request.POST, instance=empleado)
		if form.is_valid():
			form.save()
		return redirect('empleado:empleado_listar')
	return render(request, 'empleado/empleado_form.html', {'form':form})

def empleado_delete(request, id_empleado):
	empleado = Empleado.objects.get(id=id_empleado)
	if request.method == 'POST':
		empleado.delete()
		return redirect('empleado:empleado_listar')
	return render(request, 'empleado/empleado_delete.html', {'empleado':empleado})