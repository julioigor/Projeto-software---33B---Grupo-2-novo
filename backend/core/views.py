import json
from django.http import JsonResponse, HttpResponseBadRequest, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from .models import Companhia, Usuario, Servico, Localizacao, Problema


# ============================
# COMPANHIAS
# ============================
@csrf_exempt
def criar_companhia(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Méthode non supportée")

    try:
        body = json.loads(request.body)
    except:
        return HttpResponseBadRequest("JSON invalide")

    nome = body.get("nome")
    cnpj = body.get("cnpj")
    endereco = body.get("endereco")

    if not nome or not cnpj:
        return HttpResponseBadRequest("Champs 'nome' et 'cnpj' sont obligatoires")

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


# ============================
# USUARIOS
# ============================
@csrf_exempt
def criar_usuario(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Méthode non supportée")

    try:
        body = json.loads(request.body)
    except:
        return HttpResponseBadRequest("JSON invalide")

    companhia_id = body.get("companhia_id")
    nome = body.get("nome")
    email = body.get("email")
    senha_hash = body.get("senha_hash")
    cargo = body.get("cargo")

    if not companhia_id or not nome or not email or not senha_hash:
        return HttpResponseBadRequest("Champs obligatoires manquants")

    try:
        companhia = Companhia.objects.get(id=companhia_id)
    except Companhia.DoesNotExist:
        return HttpResponseBadRequest("Companhia invalide")

    usuario = Usuario.objects.create(
        companhia=companhia,
        nome=nome,
        email=email,
        senha_hash=senha_hash,
        cargo=cargo
    )

    return JsonResponse({
        "id": usuario.id,
        "companhia_id": usuario.companhia.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "cargo": usuario.cargo,
        "criado_em": usuario.criado_em,
    })


def obter_usuario(request, usuario_id):
    try:
        usuario = Usuario.objects.get(id=usuario_id)
    except Usuario.DoesNotExist:
        raise Http404("Usuário não encontrado")

    return JsonResponse({
        "id": usuario.id,
        "companhia_id": usuario.companhia.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "cargo": usuario.cargo,
        "criado_em": usuario.criado_em,
    })


# ============================
# SERVICOS
# ============================
@csrf_exempt
def criar_servico(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Méthode non supportée")

    try:
        body = json.loads(request.body)
    except:
        return HttpResponseBadRequest("JSON invalide")

    companhia_id = body.get("companhia_id")
    nome = body.get("nome")
    descricao = body.get("descricao")

    if not companhia_id or not nome:
        return HttpResponseBadRequest("Champs obligatoires manquants")

    try:
        companhia = Companhia.objects.get(id=companhia_id)
    except Companhia.DoesNotExist:
        return HttpResponseBadRequest("Companhia invalide")

    servico = Servico.objects.create(
        companhia=companhia,
        nome=nome,
        descricao=descricao
    )

    return JsonResponse({
        "id": servico.id,
        "companhia_id": servico.companhia.id,
        "nome": servico.nome,
        "descricao": servico.descricao,
    })


def obter_servico(request, servico_id):
    try:
        servico = Servico.objects.get(id=servico_id)
    except Servico.DoesNotExist:
        raise Http404("Serviço não encontrado")

    return JsonResponse({
        "id": servico.id,
        "companhia_id": servico.companhia.id,
        "nome": servico.nome,
        "descricao": servico.descricao,
    })


# ============================
# LOCALIZACOES
# ============================
@csrf_exempt
def criar_localizacao(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Méthode non supportée")

    try:
        body = json.loads(request.body)
    except:
        return HttpResponseBadRequest("JSON invalide")

    tipo = body.get("tipo")
    nome = body.get("nome")
    endereco = body.get("endereco")
    latitude = body.get("latitude")
    longitude = body.get("longitude")
    pai_id = body.get("pai_id")

    if not tipo or not nome:
        return HttpResponseBadRequest("Champs obligatoires manquants")

    pai = None
    if pai_id:
        try:
            pai = Localizacao.objects.get(id=pai_id)
        except Localizacao.DoesNotExist:
            return HttpResponseBadRequest("Localização pai invalide")

    loc = Localizacao.objects.create(
        tipo=tipo,
        nome=nome,
        endereco=endereco,
        latitude=latitude,
        longitude=longitude,
        pai=pai
    )

    return JsonResponse({
        "id": loc.id,
        "tipo": loc.tipo,
        "nome": loc.nome,
        "endereco": loc.endereco,
        "latitude": loc.latitude,
        "longitude": loc.longitude,
        "pai_id": loc.pai.id if loc.pai else None,
    })


def obter_localizacao(request, localizacao_id):
    try:
        loc = Localizacao.objects.get(id=localizacao_id)
    except Localizacao.DoesNotExist:
        raise Http404("Localização não encontrada")

    return JsonResponse({
        "id": loc.id,
        "tipo": loc.tipo,
        "nome": loc.nome,
        "endereco": loc.endereco,
        "latitude": loc.latitude,
        "longitude": loc.longitude,
        "pai_id": loc.pai.id if loc.pai else None,
    })


# ============================
# PROBLEMAS
# ============================
@csrf_exempt
def criar_problema(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Méthode non supportée")

    try:
        body = json.loads(request.body)
    except:
        return HttpResponseBadRequest("JSON invalide")

    obrigatorios = ["companhia_id", "servico_id", "criado_por_id", "titulo"]
    if any(c not in body for c in obrigatorios):
        return HttpResponseBadRequest("Champs obligatoires manquants")

    try:
        companhia = Companhia.objects.get(id=body["companhia_id"])
        servico = Servico.objects.get(id=body["servico_id"])
        criado_por = Usuario.objects.get(id=body["criado_por_id"])
    except:
        return HttpResponseBadRequest("Foreign keys invalides")

    localizacao = None
    if body.get("localizacao_id"):
        try:
            localizacao = Localizacao.objects.get(id=body["localizacao_id"])
        except Localizacao.DoesNotExist:
            return HttpResponseBadRequest("Localização invalide")

    problema = Problema.objects.create(
        companhia=companhia,
        servico=servico,
        criado_por=criado_por,
        titulo=body["titulo"],
        descricao=body.get("descricao"),
        status=body.get("status"),
        prioridade=body.get("prioridade"),
        origem=body.get("origem"),
        localizacao=localizacao,
        link_relacionado=body.get("link_relacionado"),
        fotos=body.get("fotos"),
        metadados=body.get("metadados"),
    )

    return JsonResponse({
        "id": problema.id,
        "titulo": problema.titulo,
        "companhia_id": problema.companhia.id,
        "servico_id": problema.servico.id,
        "criado_por_id": problema.criado_por.id,
        "localizacao_id": problema.localizacao.id if problema.localizacao else None,
        "descricao": problema.descricao,
        "status": problema.status,
        "prioridade": problema.prioridade,
        "origem": problema.origem,
        "link_relacionado": problema.link_relacionado,
        "fotos": problema.fotos,
        "metadados": problema.metadados,
        "data_registro": problema.data_registro,
        "data_ultima_atualizacao": problema.data_ultima_atualizacao,
    })


@csrf_exempt
def obter_problema(request, problema_id):
    try:
        problema = Problema.objects.get(id=problema_id)
    except Problema.DoesNotExist:
        raise Http404("Problema não encontrado")

    if request.method == "GET":
        # 🔹 Lecture (comme avant)
        return JsonResponse({
            "id": problema.id,
            "titulo": problema.titulo,
            "companhia_id": problema.companhia.id if problema.companhia else None,
            "servico_id": problema.servico.id if problema.servico else None,
            "criado_por_id": problema.criado_por.id if problema.criado_por else None,
            "descricao": problema.descricao,
            "status": problema.status,
            "prioridade": problema.prioridade,
            "origem": problema.origem,
            "localizacao_id": problema.localizacao.id if problema.localizacao else None,
            "link_relacionado": problema.link_relacionado,
            "fotos": problema.fotos,
            "metadados": problema.metadados,
            "data_registro": problema.data_registro,
            "data_ultima_atualizacao": problema.data_ultima_atualizacao,
        })

    elif request.method in ("PUT", "PATCH"):
        # 🔹 Mise à jour
        try:
            body = json.loads(request.body)
        except:
            return HttpResponseBadRequest("JSON invalide")

        champs_editables = [
            "titulo",
            "descricao",
            "status",
            "prioridade",
            "origem",
            "link_relacionado",
        ]

        for champ in champs_editables:
            if champ in body:
                setattr(problema, champ, body[champ])

        problema.save()

        return JsonResponse({
            "id": problema.id,
            "titulo": problema.titulo,
            "companhia_id": problema.companhia.id if problema.companhia else None,
            "servico_id": problema.servico.id if problema.servico else None,
            "criado_por_id": problema.criado_por.id if problema.criado_por else None,
            "descricao": problema.descricao,
            "status": problema.status,
            "prioridade": problema.prioridade,
            "origem": problema.origem,
            "localizacao_id": problema.localizacao.id if problema.localizacao else None,
            "link_relacionado": problema.link_relacionado,
            "fotos": problema.fotos,
            "metadados": problema.metadados,
            "data_registro": problema.data_registro,
            "data_ultima_atualizacao": problema.data_ultima_atualizacao,
        })

    else:
        return HttpResponseBadRequest("Méthode non supportée")

    
@require_GET
def listar_problemas(request):
    """
    Liste les problèmes, éventuellement filtrés par companhia_id.
    GET /api/problemas/listar/
    GET /api/problemas/listar/?companhia_id=1
    """
    companhia_id = request.GET.get("companhia_id")

    qs = Problema.objects.all().select_related("companhia", "servico", "criado_por", "localizacao")
    if companhia_id:
        qs = qs.filter(companhia_id=companhia_id)

    qs = qs.order_by("-data_registro")[:50]  # limite pour le projet

    data = []
    for p in qs:
        data.append({
            "id": p.id,
            "titulo": p.titulo,
            "descricao": p.descricao,
            "status": p.status,
            "prioridade": p.prioridade,
            "origem": p.origem,
            "companhia_id": p.companhia.id if p.companhia else None,
            "servico_id": p.servico.id if p.servico else None,
            "criado_por_id": p.criado_por.id if p.criado_por else None,
            "localizacao_id": p.localizacao.id if p.localizacao else None,
            "data_registro": p.data_registro,
            "data_ultima_atualizacao": p.data_ultima_atualizacao,
        })

    return JsonResponse(data, safe=False)
    
# ============================
# LOGIN
# ============================
@csrf_exempt
def login_usuario(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Méthode non supportée")

    try:
        body = json.loads(request.body)
    except:
        return HttpResponseBadRequest("JSON invalide")

    email = body.get("email")
    senha = body.get("senha")  # ou senha_hash

    if not email or not senha:
        return HttpResponseBadRequest("Email et mot de passe obligatoires")

    try:
        # ⚠️ Exemple naïf : à remplacer par un vrai hash
        usuario = Usuario.objects.get(email=email, senha_hash=senha)
    except Usuario.DoesNotExist:
        return HttpResponseBadRequest("Identifiants invalides")

    return JsonResponse({
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "companhia_id": usuario.companhia.id if usuario.companhia else None,
        "cargo": usuario.cargo,
    })
