from fastapi import FastAPI

from database import Base, engine

from routers import (
    usuarios,
    tutor,
    pets,
    consulta,
    banho,
    veterinario,
    funcionario,
    recepcionista
)

app = FastAPI(
    title="Pet Shop API"
)

Base.metadata.create_all(bind=engine)

app.include_router(usuarios.router)
app.include_router(tutor.router)
app.include_router(pets.router)
app.include_router(consulta.router)
app.include_router(banho.router)
app.include_router(veterinario.router)
app.include_router(funcionario.router)
app.include_router(recepcionista.router)