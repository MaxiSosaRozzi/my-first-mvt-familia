from django.urls import path
from familia.views import *


urlpatterns = [
    path('', index, name="index"),
    path('agregar/', agregar, name="agregar"),
    path('borrar/<identificador>', borrar, name="borrar"),

]