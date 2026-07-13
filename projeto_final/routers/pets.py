from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db

router = APIRouter(
    prefix="/pets",
    tags=["Pets"]
)


@router.post("/")
def adicionar_pet(
    pet: schemas.PetCreate,
    db: Session = Depends(get_db)
):
    return crud.adicionar_pet(db, pet)


@router.get("/")
def listar_pets(
    db: Session = Depends(get_db)
):
    return crud.listar_pets(db)


@router.get("/{id_pet}")
def buscar_pet(
    id_pet: int,
    db: Session = Depends(get_db)
):

    pet = crud.buscar_pet(db, id_pet)

    if pet is None:
        raise HTTPException(
            status_code=404,
            detail="Pet não encontrado."
        )

    return pet


@router.put("/{id_pet}")
def atualizar_pet(
    id_pet: int,
    pet: schemas.PetCreate,
    db: Session = Depends(get_db)
):

    return crud.atualizar_pet(
        db,
        id_pet,
        pet
    )


@router.delete("/{id_pet}")
def deletar_pet(
    id_pet: int,
    db: Session = Depends(get_db)
):

    crud.deletar_pet(db, id_pet)

    return {
        "mensagem": "Pet removido com sucesso."
    }