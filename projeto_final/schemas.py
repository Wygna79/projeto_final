from datetime import date, time
from pydantic import BaseModel, EmailStr

class UsuarioCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class Login(BaseModel):
    username: str
    password: str

class TutorCreate(BaseModel):
    nome: str
    telefone: str
    email: EmailStr
    endereco: str

class TutorUpdate(BaseModel):
    nome: str
    telefone: str
    email: EmailStr
    endereco: str

class PetCreate(BaseModel):
    nome_pet: str
    especie: str
    raca: str
    idade: int
    id_tutor: int

class PetUpdate(BaseModel):
    nome_pet: str
    especie: str
    raca: str
    idade: int
    id_tutor: int

class VeterinarioCreate(BaseModel):
    nome: str
    telefone: str
    salario: float

class VeterinarioUpdate(BaseModel):
    nome: str
    telefone: str
    salario: float

class FuncionarioCreate(BaseModel):
    nome: str
    telefone: str
    salario: float

class FuncionarioUpdate(BaseModel):
    nome: str
    telefone: str
    salario: float

class RecepcionistaCreate(BaseModel):
    nome: str
    telefone: str
    salario: float

class RecepcionistaUpdate(BaseModel):
    nome: str
    telefone: str
    salario: float

class ConsultaCreate(BaseModel):
    data_consulta: date
    horario: time
    status: str
    id_pet: int
    id_veterinario: int
    id_recepcionista: int

class ConsultaUpdate(BaseModel):
    data_consulta: date
    horario: time
    status: str
    id_pet: int
    id_veterinario: int
    id_recepcionista: int

class BanhoCreate(BaseModel):
    data_banho: date
    valor: float
    id_pet: int
    id_funcionario: int
    id_recepcionista: int

class BanhoUpdate(BaseModel):
    data_banho: date
    valor: float
    id_pet: int
    id_funcionario: int
    id_recepcionista: int

