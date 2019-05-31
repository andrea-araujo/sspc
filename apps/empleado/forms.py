from django import forms

from apps.empleado.models import Empleado


class EmpleadoForm(forms.ModelForm):

	class Meta:
		model = Empleado

		fields = [
			'nombre',
            'apellido',
            'sexo',
            'direccion',
            'telefono',
            'correo',
		]

		labels = {
			'nombre': 'Nombre(s)',
            'apellido': 'Apellido(s)',
            'sexo': 'Sexo',
            'direccion':'Direccion',
            'telefono': 'Telefono',
            'correo': 'Correo electronico',
		}

		widgets = {
			'nombre': forms.TextInput(attrs={'class' : 'form-control'}),
            'apellido': forms.TextInput(attrs={'class' : 'form-control'}),
            'sexo': forms.TextInput(attrs={'class' : 'form-control'}),
            'direccion': forms.TextInput(attrs={'class' : 'form-control'}),
            'telefono': forms.TextInput(attrs={'class' : 'form-control'}),
            'correo': forms.TextInput(attrs={'class' : 'form-control'}),
		}
			