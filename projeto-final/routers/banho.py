from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db

router = APIRouter(
    prefix="/banhos",
    tags=["Banhos"]
)

@router.post("/")
def adicionar_banho(
    banho: schemas.BanhoCreate,
    db: Session = Depends(get_db)
):
    return crud.adicionar_banho(db, banho)


@router.get("/")
def listar_banhos(
    db: Session = Depends(get_db)
):
    return crud.listar_banhos(db)


@router.get("/{id_banho}")
def buscar_banho(
    id_banho: int,
    db: Session = Depends(get_db)
):

    banho = crud.buscar_banho(db, id_banho)

    if banho is None:
        raise HTTPException(
            status_code=404,
            detail="Banho não encontrado."
        )

    return banho


@router.put("/{id_banho}")
def atualizar_banho(
    id_banho: int,
    banho: schemas.BanhoCreate,
    db: Session = Depends(get_db)
):

    return crud.atualizar_banho(
        db,
        id_banho,
        banho
    )


@router.delete("/{id_banho}")
def deletar_banho(
    id_banho: int,
    db: Session = Depends(get_db)
):

    crud.deletar_banho(db, id_banho)

    return {
        "mensagem": "Banho removido com sucesso."
    }