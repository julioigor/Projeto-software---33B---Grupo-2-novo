from django.http import JsonResponse, HttpResponseBadRequest, Http404
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Companhia
import uuid


# ===============================
# POST /companhias/ = créer
# ===============================
@csrf_exempt  # désactive CSRF pour tests POST via API (OK pour projet étudiant)
def criar_companhia(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Méthode non supportée")

    try:
        body = json.loads(request.body)
    except:
        return HttpResponseBadRequest("JSON inválido")

    nome = body.get("nome")
    cnpj = body.get("cnpj")
    endereco = body.get("endereco")

    if not nome or not cnpj:
        return HttpResponseBadRequest("Campos 'nome' et 'cnpj' são obrigatórios")

    companhia = Companhia.objects.create(
        nome=nome,
        cnpj=cnpj,
        endereco=endereco,
    )

    return JsonResponse({
        "id": companhia.id,
        "nome": companhia.nome,
        "cnpj": companhia.cnpj,
        "endereco": companhia.endereco,
        "criado_em": companhia.criado_em,
    })


# ==========================================
# GET /companhias/<id>/ = obter companhia
# ==========================================
def obter_companhia(request, companhia_id):
    try:
        companhia = Companhia.objects.get(id=companhia_id)
    except Companhia.DoesNotExist:
        raise Http404("Companhia não encontrada")

    return JsonResponse({
        "id": companhia.id,
        "nome": companhia.nome,
        "cnpj": companhia.cnpj,
        "endereco": companhia.endereco,
        "criado_em": companhia.criado_em,
    })
