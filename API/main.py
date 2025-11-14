from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from db import Base, engine
from models import Companhia
from schemas import CompanhiaCreate, CompanhiaOut
from dependencies import get_db
from datetime import datetime

app = FastAPI()

# Création des tables si non existantes
Base.metadata.create_all(bind=engine)


# ============================
#   POST /companhias
# ============================
@app.post("/companhias", response_model=CompanhiaOut)
def create_companhia(payload: CompanhiaCreate, db: Session = Depends(get_db)):

    companhia = Companhia(
        nome=payload.nome,
        cnpj=payload.cnpj,
        endereco=payload.endereco,
        criado_em=datetime.utcnow(),
    )

    db.add(companhia)
    db.commit()
    db.refresh(companhia)

    return companhia


# ============================
#   GET /companhias/{id}
# ============================
@app.get("/companhias/{id}", response_model=CompanhiaOut)
def get_companhia(id: UUID, db: Session = Depends(get_db)):
    companhia = db.query(Companhia).filter(Companhia.id == id).first()

    if not companhia:
        raise HTTPException(status_code=404, detail="Companhia não encontrada")

    return companhia
