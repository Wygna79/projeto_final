from sqlalchemy import *
from sqlalchemy.orm import relationship
from database import Base

class Usuario(Base):
    __tablename__ = "usuario"
    id_usuario = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

class Tutor(Base):
    __tablename__ = "tutor"
    id_tutor = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    telefone = Column(String(20))
    email = Column(String(100))
    endereco = Column(String(150))
    pets = relationship("Pet", back_populates="tutor")

class Pet(Base):
    __tablename__ = "pets"
    id_pet = Column(Integer, primary_key=True)
    nome_pet = Column(String(50), nullable=False)
    especie = Column(String(50))
    raca = Column(String(50))
    idade = Column(Integer)
    id_tutor = Column(
        Integer,
        ForeignKey("tutor.id_tutor")
    )

    tutor = relationship(
        "Tutor",
       back_populates="pets"
    )

class Veterinario(Base):
    __tablename__ = "veterinario"
    id_veterinario = Column(Integer, primary_key=True)
    nome = Column(String(100))
    telefone = Column(String(20))
    salario = Column(Numeric(10,2))

class Recepcionista(Base):
    __tablename__ = "recepcionista"
    id_recepcionista = Column(Integer, primary_key=True)
    nome = Column(String(100))
    telefone = Column(String(20))
    salario = Column(Numeric(10,2))

class Funcionario(Base):
    __tablename__ = "funcionario"
    id_funcionario = Column(Integer, primary_key=True)
    nome = Column(String(100))
    telefone = Column(String(20))
    salario = Column(Numeric(10,2))

class Consulta(Base):
    __tablename__ = "consulta"
    id_consulta = Column(Integer, primary_key=True)
    data_consulta = Column(Date)
    horario = Column(Time)
    status = Column(String(30))

    id_pet = Column(
        Integer,
        ForeignKey("pets.id_pet")
    )
    id_veterinario = Column(
        Integer,
        ForeignKey("veterinario.id_veterinario")
    )
    id_recepcionista = Column(
        Integer,
        ForeignKey("recepcionista.id_recepcionista")
    )

class Banho(Base):
    __tablename__ = "banho"
    id_banho = Column(Integer, primary_key=True)
    data_banho = Column(Date)
    valor = Column(Numeric(10,2))

    id_pet = Column(
        Integer,
        ForeignKey("pets.id_pet")
    )
    id_funcionario = Column(
        Integer,
        ForeignKey("funcionario.id_funcionario")
    )
    id_recepcionista = Column(
        Integer,
        ForeignKey("recepcionista.id_recepcionista")
    )