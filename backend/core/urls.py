from django.urls import path
from .views import (
    criar_companhia, obter_companhia,
    criar_usuario, obter_usuario,
    criar_servico, obter_servico,
    criar_localizacao, obter_localizacao,
    criar_problema, obter_problema, login_usuario,
    listar_problemas
)

urlpatterns = [
    # COMPANHIAS
    path("companhias/", criar_companhia),
    path("companhias/<uuid:companhia_id>/", obter_companhia),

    # USUÁRIOS
    path("usuarios/", criar_usuario),
    path("usuarios/<uuid:usuario_id>/", obter_usuario),

    # SERVIÇOS
    path("servicos/", criar_servico),
    path("servicos/<uuid:servico_id>/", obter_servico),

    # LOCALIZAÇÕES
    path("localizacoes/", criar_localizacao),
    path("localizacoes/<uuid:localizacao_id>/", obter_localizacao),

    # PROBLEMAS
    path("problemas/", criar_problema),
    path("problemas/<uuid:problema_id>/", obter_problema),
    path("problemas/listar/", listar_problemas, name="listar_problemas"),
    
    #LOGIN
    path("api/login/", login_usuario, name="login_usuario"),
]
