from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from typing import Optional, List, Any


# ============================================================
# COMPANHIAS
# ============================================================

class CompanhiaCreate(BaseModel):
    nome: str
    cnpj: str
    endereco: Optional[str] = None


class CompanhiaUpdate(BaseModel):
    nome: Optional[str] = None
    cnpj: Optional[str] = None
    endereco: Optional[str] = None


class CompanhiaOut(BaseModel):
    id: UUID
    nome: str
    cnpj: str
    endereco: Optional[str]
    criado_em: Optional[datetime]

    class Config:
        orm_mode = True



# ============================================================
# USUARIOS
# ============================================================

class UsuarioCreate(BaseModel):
    companhia_id: UUID
    nome: str
    email: str
    senha_hash: str
    cargo: Optional[str] = None


class UsuarioUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    senha_hash: Optional[str] = None
    cargo: Optional[str] = None


class UsuarioOut(BaseModel):
    id: UUID
    companhia_id: UUID
    nome: str
    email: str
    cargo: Optional[str]
    criado_em: Optional[datetime]

    class Config:
        orm_mode = True



# ============================================================
# SERVICOS
# ============================================================

class ServicoCreate(BaseModel):
    companhia_id: UUID
    nome: str
    descricao: Optional[str] = None


class ServicoUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None


class ServicoOut(BaseModel):
    id: UUID
    companhia_id: UUID
    nome: str
    descricao: Optional[str]

    class Config:
        orm_mode = True



# ============================================================
# LOCALIZACOES
# ============================================================

class LocalizacaoCreate(BaseModel):
    tipo: str
    nome: str
    endereco: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    pai_id: Optional[UUID] = None


class LocalizacaoUpdate(BaseModel):
    tipo: Optional[str] = None
    nome: Optional[str] = None
    endereco: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    pai_id: Optional[UUID] = None


class LocalizacaoOut(BaseModel):
    id: UUID
    tipo: str
    nome: str
    endereco: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    pai_id: Optional[UUID]

    class Config:
        orm_mode = True



# ============================================================
# PROBLEMAS
# ============================================================

class ProblemaCreate(BaseModel):
    companhia_id: UUID
    servico_id: UUID
    criado_por: UUID

    titulo: str
    descricao: Optional[str] = None
    status: Optional[str] = None
    prioridade: Optional[str] = None
    origem: Optional[str] = None
    localizacao_id: Optional[UUID] = None

    link_relacionado: Optional[str] = None
    fotos: Optional[Any] = None
    metadados: Optional[Any] = None


class ProblemaUpdate(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    status: Optional[str] = None
    prioridade: Optional[str] = None
    origem: Optional[str] = None
    localizacao_id: Optional[UUID] = None

    link_relacionado: Optional[str] = None
    fotos: Optional[Any] = None
    metadados: Optional[Any] = None

    data_ultima_atualizacao: Optional[datetime] = None


class ProblemaOut(BaseModel):
    id: UUID
    companhia_id: UUID
    servico_id: UUID
    criado_por: UUID

    titulo: str
    descricao: Optional[str]
    status: Optional[str]
    prioridade: Optional[str]
    origem: Optional[str]
    localizacao_id: Optional[UUID]

    link_relacionado: Optional[str]
    fotos: Optional[Any]
    metadados: Optional[Any]

    data_registro: Optional[datetime]
    data_ultima_atualizacao: Optional[datetime]

    class Config:
        orm_mode = True
