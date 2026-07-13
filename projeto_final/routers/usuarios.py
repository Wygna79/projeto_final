from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from database import get_db

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuários"]
)

@router.post("/")
def cadastrar(
    usuario: schemas.UsuarioCreate,
    db: Session = Depends(get_db)
):
    return crud.criar_usuario(db, usuario)

@router.post("/login")
def login(
    usuario: schemas.Login,
    db: Session = Depends(get_db)
):

    resultado = crud.login(db, usuario)

    if resultado is None:
        raise HTTPException(
            status_code=401,
            detail="Usuário ou senha inválidos."
        )

    return {
        "mensagem": "Login realizado com sucesso!"
    }