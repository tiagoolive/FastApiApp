from typing import List, Optional
from pydantic import BaseModel


class Usuario(BaseModel):
    id: Optional[str]
    nome: str
    telefone: str
    meusProdutos: List[Produto]
    minhas_vendas: List[Pedido]
    meus_pedidos: List[Pedido]


class Produto(BaseModel):
    id: Optional[str]
    usuario: Usuario
    nome: str
    detalhe: str
    preco: float
    disponivel: bool = False


class Pedido(BaseModel):
    id: Optional[str]
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: Optional[str] = 'Sem observações'
