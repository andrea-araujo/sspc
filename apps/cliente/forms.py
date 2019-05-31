from django import forms

from apps.cliente.models import Cliente


class ClienteForm(forms.ModelForm):

	class Meta:
		model = Cliente

		fields = [
		'nombre',
            'apellido',
            'direccion',
            'telefono',
            'correo',
		]

		labels = {
		'nombre':'Nombre(s)',
            'apellido': 'Apellidos(s)',
            'direccion': 'Direccion',
            'telefono' : 'Telefono',
            'correo' : 'Correo electronico',
		}

		widgets = {
		'nombre': forms.TextInput(attrs={'class' : 'form-control'} ),
            'apellido': forms.TextInput(attrs={'class' : 'form-control'}),
            'direccion': forms.TextInput(attrs={'class' : 'form-control'}),
            'telefono': forms.TextInput(attrs={'class' : 'form-control'}),
            'correo': forms.TextInput(attrs={'class' : 'form-control'}),
		}