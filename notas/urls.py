from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acerca', views.nosotros, name='acerca'),
    path('docente', views.docente, name='docente'),
    path('docente/crear', views.crear, name='crear'),
    path('docente/editar/<int:id>', views.editar, name='editar'),
    path('docente/eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('estudiante', views.estudiante, name='estudiante'),
    path('estudiante/crear', views.est_crear, name='est_crear'),
    path('estudiante/editar/<int:id>', views.est_editar, name='est_editar'),
    path('estudiante/eliminar/<int:id>', views.est_eliminar, name='est_eliminar'),
]