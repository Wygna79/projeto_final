from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import schemas
from database import get_db

router = APIRouter(
    prefix="/tutores",
    tags=["Tutores"]
)

@router.post("/")
def criar_tutor(
    tutor: schemas.TutorCreate,
    db: Session = Depends(get_db)
):
    return crud.criar_tutor(db, tutor)

@router.get("/")
def listar_tutores(
    db: Session = Depends(get_db)
):
    return crud.listar_tutores(db)

@router.get("/{id}")
def buscar_tutor(
    id: int,
    db: Session = Depends(get_db)
):

    tutor = crud.buscar_tutor(db, id)

    if tutor is None:
        raise HTTPException(
            status_code=404,
            detail="Tutor não encontrado."
        )

    return tutor

@router.put("/{id}")
def atualizar_tutor(
    id: int,
    tutor: schemas.TutorCreate,
    db: Session = Depends(get_db)
):

    return crud.atualizar_tutor(
        db,
        id,
        tutor
    )

@router.delete("/{id}")
def deletar_tutor(
    id: int,
    db: Session = Depends(get_db)
):

    crud.deletar_tutor(db, id)

    return {
        "mensagem": "Tutor removido com sucesso."
    }