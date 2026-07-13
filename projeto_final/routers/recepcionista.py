from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db

router = APIRouter(
    prefix="/recepcionistas",
    tags=["Recepcionistas"]
)


@router.post("/")
def adicionar_recepcionista(
    recepcionista: schemas.RecepcionistaCreate,
    db: Session = Depends(get_db)
):
    return crud.adicionar_recepcionista(db, recepcionista)


@router.get("/")
def listar_recepcionistas(
    db: Session = Depends(get_db)
):
    return crud.listar_recepcionistas(db)


@router.get("/{id_recepcionista}")
def buscar_recepcionista(
    id_recepcionista: int,
    db: Session = Depends(get_db)
):

    recepcionista = crud.buscar_recepcionista(db, id_recepcionista)

    if recepcionista is None:
        raise HTTPException(
            status_code=404,
            detail="Recepcionista não encontrado."
        )

    return recepcionista


@router.put("/{id_recepcionista}")
def atualizar_recepcionista(
    id_recepcionista: int,
    recepcionista: schemas.RecepcionistaCreate,
    db: Session = Depends(get_db)
):

    return crud.atualizar_recepcionista(
        db,
        id_recepcionista,
        recepcionista
    )


@router.delete("/{id_recepcionista}")
def deletar_recepcionista(
    id_recepcionista: int,
    db: Session = Depends(get_db)
):

    crud.deletar_recepcionista(db, id_recepcionista)

    return {
        "mensagem": "Recepcionista removido com sucesso."
    }