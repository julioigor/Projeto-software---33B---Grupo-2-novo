from django.urls import path
from .views import criar_companhia, obter_companhia

urlpatterns = [
    path("companhias/", criar_companhia),
    path("companhias/<uuid:companhia_id>/", obter_companhia),
]
