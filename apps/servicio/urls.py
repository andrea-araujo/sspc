from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.servicio.views import index_servicio, servicio_view, servicio_list, servicio_edit, servicio_delete

urlpatterns = [
    url(r'^index$',login_required(index_servicio), name='indexServicio'),
    url(r'^nuevo$',login_required(servicio_view), name='servicio_crear'),
    url(r'^listar$', login_required(servicio_list), name='servicio_listar'),
    url(r'^editar/(?P<id_servicio>\d+)/$', login_required(servicio_edit), name='servicio_editar'),
    url(r'^eliminar/(?P<id_servicio>\d+)/$', login_required(servicio_delete), name='servicio_eliminar'),
]
