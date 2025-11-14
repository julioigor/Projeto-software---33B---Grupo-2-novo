import uuid
from django.db import models


# =========================
# COMPANHIAS
# =========================
class Companhia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=50)
    endereco = models.TextField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


# =========================
# USUARIOS
# =========================
class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    companhia = models.ForeignKey(Companhia, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    senha_hash = models.TextField()
    cargo = models.CharField(max_length=255, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


# =========================
# SERVICOS
# =========================
class Servico(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    companhia = models.ForeignKey(Companhia, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome


# =========================
# LOCALIZACOES
# =========================
class Localizacao(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    endereco = models.TextField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    pai = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome


# =========================
# PROBLEMAS
# =========================
class Problema(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    companhia = models.ForeignKey(Companhia, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    criado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

    titulo = models.CharField(max_length=255)
    descricao = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    prioridade = models.CharField(max_length=255, null=True, blank=True)
    origem = models.CharField(max_length=255, null=True, blank=True)

    localizacao = models.ForeignKey(Localizacao, null=True, blank=True, on_delete=models.SET_NULL)

    link_relacionado = models.TextField(null=True, blank=True)
    fotos = models.JSONField(null=True, blank=True)
    metadados = models.JSONField(null=True, blank=True)

    data_registro = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
