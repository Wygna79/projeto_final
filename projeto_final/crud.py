from sqlalchemy.orm import Session
from passlib.context import CryptContext

import models
import schemas

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# USUARIO --------------------------------------------------
def criar_usuario(db: Session, usuario: schemas.UsuarioCreate):
    senha_hash = pwd_context.hash(usuario.password)
    novo_usuario = models.Usuario(
        username=usuario.username,
        email=usuario.email,
        password=senha_hash
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario

def login(db: Session, dados: schemas.Login):
    usuario = db.query(models.Usuario).filter(
        models.Usuario.username == dados.username
    ).first()
    if usuario is None:
        return None
    if not pwd_context.verify(
        dados.password,
        usuario.password
    ):
        return None

    return usuario

# TUTOR --------------------------------------------------
def criar_tutor(db: Session, tutor: schemas.TutorCreate):
    novo_tutor = models.Tutor(**tutor.model_dump())
    db.add(novo_tutor)
    db.commit()
    db.refresh(novo_tutor)

    return novo_tutor

def listar_tutores(db: Session):
    return db.query(models.Tutor).all()

def buscar_tutor(db: Session, id_tutor: int):
    return db.query(models.Tutor).filter(
        models.Tutor.id_tutor == id_tutor
    ).first()

def atualizar_tutor(
    db: Session,
    id_tutor: int,
    tutor: schemas.TutorCreate
):
    tutor_db = buscar_tutor(db, id_tutor)
    if tutor_db is None:
        return None
    dados = tutor.model_dump()
    for campo, valor in dados.items():
        setattr(tutor_db, campo, valor)
    db.commit()
    db.refresh(tutor_db)

    return tutor_db

def deletar_tutor(db: Session, id_tutor: int):
    tutor = buscar_tutor(db, id_tutor)
    if tutor:
        db.delete(tutor)
        db.commit()

# PETS --------------------------------------------------
def adicionar_pet(db: Session, pet: schemas.PetCreate):

    novo_pet = models.Pet(**pet.model_dump())

    db.add(novo_pet)
    db.commit()
    db.refresh(novo_pet)

    return novo_pet


# READ (Listar)
def listar_pets(db: Session):

    return db.query(models.Pet).all()


# READ (Buscar por ID)
def buscar_pet(db: Session, id_pet: int):

    return db.query(models.Pet).filter(
        models.Pet.id_pet == id_pet
    ).first()


# UPDATE
def atualizar_pet(
    db: Session,
    id_pet: int,
    pet: schemas.PetCreate
):

    pet_db = buscar_pet(db, id_pet)

    if pet_db is None:
        return None

    dados = pet.model_dump()

    for campo, valor in dados.items():
        setattr(pet_db, campo, valor)

    db.commit()
    db.refresh(pet_db)

    return pet_db


# DELETE
def deletar_pet(
    db: Session,
    id_pet: int
):

    pet = buscar_pet(db, id_pet)

    if pet is None:
        return None

    db.delete(pet)
    db.commit()

    return pet

# VETERINARIO --------------------------------------------------
def adicionar_pet(db: Session, pet: schemas.PetCreate):

    novo_pet = models.Pet(**pet.model_dump())

    db.add(novo_pet)
    db.commit()
    db.refresh(novo_pet)

    return novo_pet


# READ (Listar)
def listar_pets(db: Session):

    return db.query(models.Pet).all()


# READ (Buscar por ID)
def buscar_pet(db: Session, id_pet: int):

    return db.query(models.Pet).filter(
        models.Pet.id_pet == id_pet
    ).first()


# UPDATE
def atualizar_pet(
    db: Session,
    id_pet: int,
    pet: schemas.PetCreate
):

    pet_db = buscar_pet(db, id_pet)

    if pet_db is None:
        return None

    dados = pet.model_dump()

    for campo, valor in dados.items():
        setattr(pet_db, campo, valor)

    db.commit()
    db.refresh(pet_db)

    return pet_db


# DELETE
def deletar_pet(
    db: Session,
    id_pet: int
):

    pet = buscar_pet(db, id_pet)

    if pet is None:
        return None

    db.delete(pet)
    db.commit()

    return pet

# FUNCIONÁRIO --------------------------------------------------
def adicionar_funcionario(
    db: Session,
    funcionario: schemas.FuncionarioCreate
):

    novo_funcionario = models.Funcionario(
        **funcionario.model_dump()
    )

    db.add(novo_funcionario)
    db.commit()
    db.refresh(novo_funcionario)

    return novo_funcionario


# READ (Listar)
def listar_funcionarios(db: Session):

    return db.query(models.Funcionario).all()


# READ (Buscar por ID)
def buscar_funcionario(
    db: Session,
    id_funcionario: int
):

    return db.query(models.Funcionario).filter(
        models.Funcionario.id_funcionario == id_funcionario
    ).first()


# UPDATE
def atualizar_funcionario(
    db: Session,
    id_funcionario: int,
    funcionario: schemas.FuncionarioCreate
):

    funcionario_db = buscar_funcionario(
        db,
        id_funcionario
    )

    if funcionario_db is None:
        return None

    dados = funcionario.model_dump()

    for campo, valor in dados.items():
        setattr(funcionario_db, campo, valor)

    db.commit()
    db.refresh(funcionario_db)

    return funcionario_db


# DELETE
def deletar_funcionario(
    db: Session,
    id_funcionario: int
):

    funcionario = buscar_funcionario(
        db,
        id_funcionario
    )

    if funcionario is None:
        return None

    db.delete(funcionario)
    db.commit()

    return funcionario

# RECEPCIONISTA --------------------------------------------------
def adicionar_recepcionista(
    db: Session,
    recepcionista: schemas.RecepcionistaCreate
):

    nova_recepcionista = models.Recepcionista(
        **recepcionista.model_dump()
    )

    db.add(nova_recepcionista)
    db.commit()
    db.refresh(nova_recepcionista)

    return nova_recepcionista


# READ (Listar)
def listar_recepcionistas(db: Session):

    return db.query(models.Recepcionista).all()


# READ (Buscar por ID)
def buscar_recepcionista(
    db: Session,
    id_recepcionista: int
):

    return db.query(models.Recepcionista).filter(
        models.Recepcionista.id_recepcionista == id_recepcionista
    ).first()


# UPDATE
def atualizar_recepcionista(
    db: Session,
    id_recepcionista: int,
    recepcionista: schemas.RecepcionistaCreate
):

    recepcionista_db = buscar_recepcionista(
        db,
        id_recepcionista
    )

    if recepcionista_db is None:
        return None

    dados = recepcionista.model_dump()

    for campo, valor in dados.items():
        setattr(recepcionista_db, campo, valor)

    db.commit()
    db.refresh(recepcionista_db)

    return recepcionista_db


# DELETE
def deletar_recepcionista(
    db: Session,
    id_recepcionista: int
):

    recepcionista = buscar_recepcionista(
        db,
        id_recepcionista
    )

    if recepcionista is None:
        return None

    db.delete(recepcionista)
    db.commit()

    return recepcionista

# CONSULTA --------------------------------------------------
from sqlalchemy.orm import Session
import models
import schemas


# CREATE
def adicionar_consulta(
    db: Session,
    consulta: schemas.ConsultaCreate
):

    nova_consulta = models.Consulta(
        **consulta.model_dump()
    )

    db.add(nova_consulta)
    db.commit()
    db.refresh(nova_consulta)

    return nova_consulta


# READ (Listar)
def listar_consultas(db: Session):

    return db.query(models.Consulta).all()


# READ (Buscar por ID)
def buscar_consulta(
    db: Session,
    id_consulta: int
):

    return db.query(models.Consulta).filter(
        models.Consulta.id_consulta == id_consulta
    ).first()


# UPDATE
def atualizar_consulta(
    db: Session,
    id_consulta: int,
    consulta: schemas.ConsultaCreate
):

    consulta_db = buscar_consulta(
        db,
        id_consulta
    )

    if consulta_db is None:
        return None

    dados = consulta.model_dump()

    for campo, valor in dados.items():
        setattr(consulta_db, campo, valor)

    db.commit()
    db.refresh(consulta_db)

    return consulta_db


# DELETE
def deletar_consulta(
    db: Session,
    id_consulta: int
):

    consulta = buscar_consulta(
        db,
        id_consulta
    )

    if consulta is None:
        return None

    db.delete(consulta)
    db.commit()

    return consulta

# BANHO --------------------------------------------------
def adicionar_banho(
    db: Session,
    banho: schemas.BanhoCreate
):

    novo_banho = models.Banho(
        **banho.model_dump()
    )

    db.add(novo_banho)
    db.commit()
    db.refresh(novo_banho)

    return novo_banho


# READ (Listar)
def listar_banhos(db: Session):

    return db.query(models.Banho).all()


# READ (Buscar por ID)
def buscar_banho(
    db: Session,
    id_banho: int
):

    return db.query(models.Banho).filter(
        models.Banho.id_banho == id_banho
    ).first()


# UPDATE
def atualizar_banho(
    db: Session,
    id_banho: int,
    banho: schemas.BanhoCreate
):

    banho_db = buscar_banho(
        db,
        id_banho
    )

    if banho_db is None:
        return None

    dados = banho.model_dump()

    for campo, valor in dados.items():
        setattr(banho_db, campo, valor)

    db.commit()
    db.refresh(banho_db)

    return banho_db


# DELETE
def deletar_banho(
    db: Session,
    id_banho: int
):

    banho = buscar_banho(
        db,
        id_banho
    )

    if banho is None:
        return None

    db.delete(banho)
    db.commit()

    return banho