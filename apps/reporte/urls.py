from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.reporte.views import index_reporte, reporte_view, reporte_list, reporte_edit, reporte_delete

urlpatterns = [
	url(r'^index$',login_required(index_reporte), name='index'),
	url(r'^nuevo$',login_required(reporte_view), name='reporte_nuevo'),
	url(r'^listar$', login_required(reporte_list), name='reporte_listar'),
	url(r'^editar/(?P<id_reporte>\d+)/$', login_required(reporte_edit), name='reporte_editar'),
	url(r'^eliminar/(?P<id_reporte>\d+)/$', login_required(reporte_delete), name='reporte_eliminar'),
]

