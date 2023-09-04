from django.urls import path
from .views import *
from . import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='home'),

    #Busqueda Modelos
    path('buscar_maestro/', BuscarMaestro, name="buscar_maestro"),
    path('buscar1/', views.buscar1, name="buscar1"),
    path('buscar_materia/', views.BuscarMateria, name="buscar_materia"),
    path('buscar2/', views.buscar2, name="buscar2"),
    path('buscar_alumno/', BuscarAlumno, name="buscar_alumno"),
    path('buscar3/', views.buscar3, name="buscar3"),
    path('buscar_director/', BuscarDirector, name="buscar_director"),
    path('buscar4/', views.buscar4, name="buscar4"),

    #CBV Alumnos
    path('alumnos/', AlumnosList.as_view(), name='alumnos'),
    path('create_alumno/', AlumnosCreate.as_view(), name='create_alumno'),
    path('update_alumno/<int:pk>/', AlumnosUpdate.as_view(), name='update_alumno'),
    path('delete_alumno/<int:pk>/', AlumnosDelete.as_view(), name='delete_alumno'),

    #CBV Materias
    path('materias/', MateriasList.as_view(), name='materias'),
    path('create_materia/', MateriasCreate.as_view(), name='create_materia'),
    path('update_materia/<int:pk>/', MateriasUpdate.as_view(), name='update_materia'),
    path('delete_materia/<int:pk>/', MateriasDelete.as_view(), name='delete_materia'),

    #CBV Maestros
    path('maestros/', MaestrosList.as_view(), name='maestros'),
    path('create_maestro/', MaestrosCreate.as_view(), name='create_maestro'),
    path('update_maestro/<int:pk>/', MaestrosUpdate.as_view(), name='update_maestro'),
    path('delete_maestro/<int:pk>/', MaestrosDelete.as_view(), name='delete_maestro'),

     #CBV Maestros
    path('directores/', DirectoresList.as_view(), name='directores'),
    path('create_director/', DirectoresCreate.as_view(), name='create_director'),
    path('update_director/<int:pk>/', DirectoresUpdate.as_view(), name='update_director'),
    path('delete_director/<int:pk>/', DirectoresDelete.as_view(), name='delete_director'),

    #Login / Logout / Registro
    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name='aplicacion/logout.html'), name='logout'),
    path('registro/', register, name='registro'),

    #Editar Perfil
    path('editar_perfil/', editarPerfil, name='editar_perfil'),
    path('agregar_avatar/', agregarAvatar, name='agregar_avatar'),


]   
