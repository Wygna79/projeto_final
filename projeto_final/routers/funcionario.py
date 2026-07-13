from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db

router = APIRouter(
    prefix="/funcionarios",
    tags=["Funcionários"]
)


@router.post("/")
def adicionar_funcionario(
    funcionario: schemas.FuncionarioCreate,
    db: Session = Depends(get_db)
):
    return crud.adicionar_funcionario(db, funcionario)


@router.get("/")
def listar_funcionarios(
    db: Session = Depends(get_db)
):
    return crud.listar_funcionarios(db)


@router.get("/{id_funcionario}")
def buscar_funcionario(
    id_funcionario: int,
    db: Session = Depends(get_db)
):

    funcionario = crud.buscar_funcionario(db, id_funcionario)

    if funcionario is None:
        raise HTTPException(
            status_code=404,
            detail="Funcionário não encontrado."
        )

    return funcionario


@router.put("/{id_funcionario}")
def atualizar_funcionario(
    id_funcionario: int,
    funcionario: schemas.FuncionarioCreate,
    db: Session = Depends(get_db)
):

    return crud.atualizar_funcionario(
        db,
        id_funcionario,
        funcionario
    )


@router.delete("/{id_funcionario}")
def deletar_funcionario(
    id_funcionario: int,
    db: Session = Depends(get_db)
):

    crud.deletar_funcionario(db, id_funcionario)

    return {
        "mensagem": "Funcionário removido com sucesso."
    }