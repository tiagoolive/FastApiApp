from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()


class Animal(BaseModel):
    id: Optional[str]
    nome: str
    idade: int
    sexo: str
    cor: str


banco: List[Animal] = []


@app.get('/animais')
async def listar_animais():
    return banco


@app.get('/animais/{id}')
async def obter_animal(id: str):
    for animal in banco:
        if animal.id == id:
            return animal
    return {'erro': 'Animal não localizado'}


@app.post('/animais')
async def criar_animal(animal: Animal):
    animal.id = str(uuid4())
    banco.append(animal)
    return None


@app.delete('/animais/{id}')
async def deletar_animal(id: str):
    for animal in banco:
      if animal.id == id:
        banco.remove(animal)
        return {'status': 'Animal Removido'}

    return {'erro': 'Animal não localizado'}
      