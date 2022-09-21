from typing import Optional, List
from pydantic import BaseModel


class ProdutoSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    preco: float
    disponivel: bool

    class Config:
        orm_mode = True

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    senha: str
    produtos: list[ProdutoSimples] = []

    class config:
        orm_mode = True

class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str

    class config:
        orm_mode = True


class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float     
    disponivel: bool = False
    usuario_id: Optional[int]
    # usuario: Optional[UsuarioSimples]

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
    quantidade: int
    usuario_id: Optional[int]
    produto_id: Optional[int]
    local_entrega: str
    tipo_entrega: str
    observacao: Optional[str] = 'Sem observações'
    #usuario: Optional[Usuario]
    produto: Optional[Produto]

    class Config:
        orm_mode = True
