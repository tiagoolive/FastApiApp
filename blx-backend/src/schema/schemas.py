from typing import Optional
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

class LoginData(BaseModel):
    senha: str
    telefone: str


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


class Pedido(BaseModel):
    id: Optional[int]
    quantidade: int
    local_entrega: Optional[str]
    tipo_entrega: str
    observacao: Optional[str] = 'Sem observações'

    usuario_id: Optional[int]
    produto_id: Optional[int]
    
    #usuario: Optional[Usuario]
    produto: Optional[ProdutoSimples]

    class Config:
        orm_mode = True
