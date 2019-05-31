from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required
from apps.cliente.views import index_cliente, cliente_view, cliente_list, cliente_edit, cliente_delete


urlpatterns = [
    url(r'^$', login_required(index_cliente), name='indexCliente'),
    url(r'^nuevo$', login_required(cliente_view), name='cliente_nuevo'),
    url(r'^listar$', login_required(cliente_list), name='cliente_listar'),
    url(r'^editar/(?P<id_cliente>\d+)/$', login_required(cliente_edit), name='cliente_editar'),
    url(r'^eliminar/(?P<id_cliente>\d+)/$', login_required(cliente_delete), name='cliente_eliminar'),
]
