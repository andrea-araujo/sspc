from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.empleado.views import index_empleado, empleado_view, empleado_list, empleado_edit, empleado_delete


urlpatterns = [
    url(r'^$',login_required(index_empleado), name='indexEmpleado'),
    url(r'^nuevo$', login_required(empleado_view), name='empleado_nuevo'),
    url(r'^listar$', login_required(empleado_list), name='empleado_listar'),
    url(r'^editar/(?P<id_empleado>\d+)/$', login_required(empleado_edit), name='empleado_editar'),
    url(r'^eliminar/(?P<id_empleado>\d+)/$', login_required(empleado_delete), name='empleado_eliminar'),

]
