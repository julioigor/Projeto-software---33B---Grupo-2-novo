import uuid
from sqlalchemy import (
    Column, String, Text, ForeignKey, TIMESTAMP,
    Float, JSON
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from db import Base


# ============================
# TABELA: companhias
# ============================
class Companhia(Base):
    __tablename__ = "companhias"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = Column(String)
    cnpj = Column(String)
    endereco = Column(Text)
    criado_em = Column(TIMESTAMP)

    # relations
    usuarios = relationship("Usuario", back_populates="companhia")
    servicos = relationship("Servico", back_populates="companhia")
    problemas = relationship("Problema", back_populates="companhia")


# ============================
# TABELA: usuarios
# ============================
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    companhia_id = Column(UUID(as_uuid=True), ForeignKey("companhias.id"))

    nome = Column(String)
    email = Column(String)
    senha_hash = Column(Text)
    cargo = Column(String)
    criado_em = Column(TIMESTAMP)

    # relations
    companhia = relationship("Companhia", back_populates="usuarios")
    problemas_criados = relationship("Problema", back_populates="criado_por_user")


# ============================
# TABELA: servicos
# ============================
class Servico(Base):
    __tablename__ = "servicos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    companhia_id = Column(UUID(as_uuid=True), ForeignKey("companhias.id"))

    nome = Column(String)
    descricao = Column(Text)

    # relations
    companhia = relationship("Companhia", back_populates="servicos")
    problemas = relationship("Problema", back_populates="servico")


# ============================
# TABELA: localizacoes
# ============================
class Localizacao(Base):
    __tablename__ = "localizacoes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    tipo = Column(String)
    nome = Column(String)
    endereco = Column(Text)
    latitude = Column(Float)
    longitude = Column(Float)

    pai_id = Column(UUID(as_uuid=True), ForeignKey("localizacoes.id"), nullable=True)

    # self relation
    pai = relationship("Localizacao", remote_side=[id])

    problemas = relationship("Problema", back_populates="localizacao")


# ============================
# TABELA: problemas
# ============================
class Problema(Base):
    __tablename__ = "problemas"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    companhia_id = Column(UUID(as_uuid=True), ForeignKey("companhias.id"))
    servico_id = Column(UUID(as_uuid=True), ForeignKey("servicos.id"))
    criado_por = Column(UUID(as_uuid=True), ForeignKey("usuarios.id"))

    titulo = Column(String)
    descricao = Column(Text)
    status = Column(String)
    prioridade = Column(String)
    origem = Column(String)
    localizacao_id = Column(UUID(as_uuid=True), ForeignKey("localizacoes.id"))

    link_relacionado = Column(Text)
    fotos = Column(JSON)
    metadados = Column(JSON)

    data_registro = Column(TIMESTAMP)
    data_ultima_atualizacao = Column(TIMESTAMP)

    # relations
    companhia = relationship("Companhia", back_populates="problemas")
    servico = relationship("Servico", back_populates="problemas")
    criado_por_user = relationship("Usuario", back_populates="problemas_criados")

    localizacao = relationship("Localizacao", back_populates="problemas")
