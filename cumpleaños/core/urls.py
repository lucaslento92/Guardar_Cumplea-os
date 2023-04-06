from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("acerca_de", views.acerca_de, name="acerca_de"),
    path("agregar_cumple", views.agregar_cumple, name="agregar_cumple"),
    path("cumple_guardado", views.cumple_guardado, name="cumple_guardado"),
]