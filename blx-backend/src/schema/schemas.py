from optparse import Option
from typing import Optional
from pydantic import BaseModel


class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    senha: str
    # produtos: List[Produto] = []

    class config:
        orm_mode = True


class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float     
    disponivel: bool = False
    usuario_id: Optional[int]
    # usuario: Optional[Usuario]

    class Config:
        orm_mode = True

class ProdutoSimples(BaseModel):
    id: Optional[int]
    nome: str
    preco: float

    class Config:
        orm_mode = True


class Pedido(BaseModel):
    id: Optional[int]
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observações'
