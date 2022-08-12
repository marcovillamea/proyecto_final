from cmath import inf
from django.urls import path
from viajes.views import verPaquetes, verHotel, verVuelo, formulario_paquete,formulario_vuelo,formulario_hotel,list_all,delete

from viajes.views import viajeformulario, search_products


urlpatterns = [
    path("formulario/", viajeformulario, name= "formulario"),
    path("search_products/",search_products, name = "search products"),
    path("viajes-paquetes/",verPaquetes),
    path("viajes-hotels/",verHotel),
    path("viajes-vuelos/",verVuelo),
    path("create-paquete/", formulario_paquete),
    path("create-vuelo/", formulario_vuelo),
    path("create-hotel/", formulario_hotel),
    path("lista-all/", list_all, name="list all"),
    path("delete/<int:pk>/", delete, name="delete")
]
