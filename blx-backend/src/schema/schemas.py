from typing import List, Optional
from pydantic import BaseModel


class Usuario(BaseModel):
    id: Optional[str]
    nome: str
    telefone: str


class Produto(BaseModel):
    id: Optional[str]
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False

    class Config:
        orm_mode = True


class Pedido(BaseModel):
    id: Optional[str]
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observações'
