from django import forms

from apps.herramienta.models import Herramienta


class HerramientaForm(forms.ModelForm):

	class Meta:
		model = Herramienta

		fields = [
			'nombre',
			'fabricante',
			'costo',
		]

		labels = {
			'nombre': 'Herramienta',
			'fabricante': 'Fabricante',
			'costo': 'Costo',
		}

		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'fabricante': forms.TextInput(attrs={'class':'form-control'}),
			'costo': forms.TextInput(attrs={'class':'form-control'}),
		}
