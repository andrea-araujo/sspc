from django import forms

from apps.servicio.models import Servicio


class ServicioForm(forms.ModelForm):

	class Meta:
		model = Servicio

		fields = [
			'nombre',
			'descripcion',
			'costo',
		]

		labels = {
			'nombre': 'Servicio',
			'descripcion': 'Descripcion de servicio',
			'costo': 'Costo',
		}

		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'descripcion': forms.Textarea(attrs={'class':'form-control'}),
			'costo': forms.TextInput(attrs={'class':'form-control'}),
		}
