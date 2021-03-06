from django.conf.urls import url
from personas.views import Personas, CrearPersona,EditarPersona, ReportePersonasExcel, Bienvenida, DetallePersona, ModificarPersona,ReporteEDPExcel,ReporteODCExcel,ficha
from . import models
from . import views

urlpatterns = [
    #url(r'^',include('seguridad.urls',namespace='seguridad')),
    url(r'^$',views.Bienvenida.as_view(), name="bienvenida"),
    url(r'^crear_persona/$',views.CrearPersona.as_view(), name="crear_persona"),
    url(r'^personas/$',Personas.as_view(), name="personas"),
    url(r'^ficha/$',ficha.as_view(), name="ficha"),
    #url(r'^detail/(?P<dni>[-\w]+)/$',views.EditarPersona.as_view(), name="editar_persona"),
    url(r'^detail/(?P<id_Persona>\d+)/$',views.EditarPersona.as_view(), name="editar_persona"),
    url(r'^reporte_personas_excel/$',ReportePersonasExcel.as_view(), name="reporte_personas_excel"),

    url(r'^reporte_edp_excel/$',ReporteEDPExcel.as_view(), name="reporte_edp_excel"),
    url(r'^reporte_odc_excel/$',ReporteODCExcel.as_view(), name="reporte_odc_excel"),

    url(r'^detalle_persona/(?P<pk>\d+)/$', DetallePersona.as_view(), name="detalle_persona"),
    url(r'^modificar_persona/(?P<pk>\d+)/$',ModificarPersona.as_view(), name="modificar_persona"),

    url(r'^polls/$', views.upload, name='uplink'),
    url(r'^polls/import/', views.import_data, name="import"),
    url(r'^polls/import_EDP/', views.import_EDP_ODC, name="import_EDP_ODC"),
    url(r'^polls/export/(.*)', views.export_data, name="export"),
    url(r'^polls/import_sheet/', views.import_sheet, name="import_sheet"),
    url(r'^ctto/export/', views.export_r5, name="export_r5"),


    url(r'^prueba/',views.prueba, name="prueba"),

]
