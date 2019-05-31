from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.herramienta.views import index_herramientas, herramienta_view, herramienta_list, herramienta_edit, herramienta_delete

urlpatterns = [
    url(r'^index$',login_required(index_herramientas), name='indexHerramienta'),
    url(r'^nuevo$',login_required(herramienta_view), name='herramienta_crear'),
    url(r'^listar$', login_required(herramienta_list), name='herramienta_listar'),
    url(r'^editar/(?P<id_herramienta>\d+)/$', login_required(herramienta_edit), name='herramienta_editar'),
    url(r'^eliminar/(?P<id_herramienta>\d+)/$', login_required(herramienta_delete), name='herramienta_eliminar'),
]
