from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('<int:id>/', views.ver_usuario, name='ver_usuario'),
    path('agregar/', views.agregar_usuario, name='agregar_usuario'),
    path('editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('borrar/<int:id>/', views.borrar_usuario, name='borrar_usuario'),
]
