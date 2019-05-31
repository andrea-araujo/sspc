from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.cliente.forms import ClienteForm
from apps.cliente.models import Cliente

def index_cliente(request):
    return render(request, 'cliente/index.html')



def cliente_view(request):
	if request.method=='POST':
		form=ClienteForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('cliente:indexCliente')
	else:
		form=ClienteForm()
	return render(request,'cliente/cliente_form.html',{'form': form})


def cliente_list(request):
	cliente = Cliente.objects.all().order_by('id')
	contexto= {'cliente': cliente}
	return render(request, 'cliente/cliente_list.html', contexto)
	

def cliente_edit(request, id_cliente):
	cliente = Cliente.objects.get(id=id_cliente)
	if request.method == 'GET':
		form = ClienteForm(instance=cliente)
	else:
		form = ClienteForm(request.POST, instance=cliente)
		if form.is_valid():
			form.save()
		return redirect('cliente:cliente_listar')
	return render(request, 'cliente/cliente_form.html', {'form':form})

def cliente_delete(request, id_cliente):
	cliente = Cliente.objects.get(id=id_cliente)
	if request.method == 'POST':
		cliente.delete()
		return redirect('cliente:cliente_listar')
	return render(request, 'cliente/cliente_delete.html', {'cliente':cliente})