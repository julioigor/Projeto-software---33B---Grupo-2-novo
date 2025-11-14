from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class CompanhiaCreate(BaseModel):
    nome: str
    cnpj: str
    endereco: str | None = None

class CompanhiaOut(BaseModel):
    id: UUID
    nome: str
    cnpj: str
    endereco: str | None = None
    criado_em: datetime | None = None

    class Config:
        orm_mode = True
