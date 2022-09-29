from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.repositorios.repositorio_pedido import RepositorioPedido
from src.infra.sqlalchemy.config.database import get_db
from src.schema.schemas import Pedido


router = APIRouter()


@router.get('/pedidos/', response_model=list[Pedido])
async def listar_pedidos(session: Session = Depends(get_db)):
    pedidos = RepositorioPedido(session).listar()
    return pedidos


@router.get('/pedidos/{id}')
async def exibir_pedido(id: int, session: Session = Depends(get_db)):
    try:
        pedido = RepositorioPedido(session).buscar_por_id(id)
        return pedido
    except:
        raise HTTPException(
            status_code=404, detail=f'Não há um pedido com o id={id}')


@router.get('/pedidos/{usuario_id}/compras', response_model=list[Pedido])
async def listar_pedidos_por_usuario(usuario_id: int, session: Session = Depends(get_db)):
    pedidos = RepositorioPedido(
        session).listar_meus_pedidos_por_usuario_id(usuario_id)
    return pedidos


@router.get('/pedidos/{usuario_id}/vendas', response_model=list[Pedido])
async def listar_vendas(usuario_id: int, session: Session = Depends(get_db)):
    pedidos = RepositorioPedido(
        session).listar_minhas_vendas_por_usuario_id(usuario_id)
    return pedidos


@router.post('/pedidos', status_code=status.HTTP_201_CREATED, response_model=Pedido)
async def fazer_pedidos(pedido: Pedido, session: Session = Depends(get_db)):
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
