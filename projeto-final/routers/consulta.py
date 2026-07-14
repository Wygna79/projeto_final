from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db

router = APIRouter(
    prefix="/consultas",
    tags=["Consultas"]
)


@router.post("/")
def adicionar_consulta(
    consulta: schemas.ConsultaCreate,
    db: Session = Depends(get_db)
):
    return crud.adicionar_consulta(db, consulta)


@router.get("/")
def listar_consultas(
    db: Session = Depends(get_db)
):
    return crud.listar_consultas(db)


@router.get("/{id_consulta}")
def buscar_consulta(
    id_consulta: int,
    db: Session = Depends(get_db)
):

    consulta = crud.buscar_consulta(db, id_consulta)

    if consulta is None:
        raise HTTPException(
            status_code=404,
            detail="Consulta não encontrada."
        )

    return consulta


@router.put("/{id_consulta}")
def atualizar_consulta(
    id_consulta: int,
    consulta: schemas.ConsultaCreate,
    db: Session = Depends(get_db)
):

    return crud.atualizar_consulta(
        db,
        id_consulta,
        consulta
    )


@router.delete("/{id_consulta}")
def deletar_consulta(
    id_consulta: int,
    db: Session = Depends(get_db)
):

    crud.deletar_consulta(db, id_consulta)

    return {
        "mensagem": "Consulta removida com sucesso."
    }