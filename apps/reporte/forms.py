from django import forms

from apps.reporte.models import Reporte


class ReporteForm(forms.ModelForm):

	class Meta:
		model= Reporte

		fields=[
			'fecha',
	    	'empleado',
	    	'cliente',
	    	'servicio',
	    	'herramienta',
	    	'descripcion',
		]

		labels={
			'fecha': "Fecha",
	    	'empleado': "Empleado",
	    	'cliente': "Cliente",
	    	'servicio': "Servicio(s) realizado(s)",
	    	'herramienta': "Herramienta(s) utilizada(s)",
	    	'descripcion': "Descripcion de servicio(s)",
		}
		widgets={
			'fecha':forms.TextInput(attrs={'class':'form-control'}),
	    	'empleado': forms.Select(attrs={'class' : 'form-control'}),
	    	'cliente': forms.Select(attrs={'class' : 'form-control'}),
	    	'servicio': forms.CheckboxSelectMultiple(),
	    	'herramienta': forms.CheckboxSelectMultiple(),
	    	'descripcion': forms.Textarea(attrs={'class':'form-control'}),
		}



			