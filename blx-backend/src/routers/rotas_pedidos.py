from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.repositorios.repositorio_pedido import RepositorioPedido
from src.infra.sqlalchemy.config.database import get_db
from src.schema.schemas import Pedido


router = APIRouter()

@router.get('/pedidos', response_model=list[Pedido])
async def listar_pedidos(session: Session = Depends(get_db)):
    pedidos = RepositorioPedido(session).listar()
    return pedidos

@router.get('/pedidos/{id}')
async def exibir_pedido(id: int, session: Session = Depends(get_db)):
    pedido = RepositorioPedido(session).buscarPorId(id)
    if not pedido:
        raise HTTPException(status_code=404, detail='Não há um pedido com este ID')

    return pedido

@router.post('/pedidos', status_code=status.HTTP_201_CREATED, response_model=Pedido)
async def criar_pedidos(pedido: Pedido, session: Session = Depends(get_db)):
    pedido_criado = RepositorioPedido(session).criar(pedido)
    return pedido_criado


@router.put('/pedidos/{id}', response_model=Pedido)
async def atualizar_pedido(id: int, pedido: Pedido, session: Session = Depends(get_db)):
    RepositorioPedido(session).editar(id, pedido)
    pedido.id = id
    return pedido


@router.delete('/pedidos/{id}')
async def remover_pedido(id: int, session: Session = Depends(get_db)):
    RepositorioPedido(session).remover(id)
    return {'Mensagem': 'Pedido Removido'}