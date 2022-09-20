from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto
from src.infra.sqlalchemy.config.database import get_db
from src.schema.schemas import Produto, ProdutoSimples


router = APIRouter()

@router.get('/produtos', response_model=list[ProdutoSimples])
async def listar_produtos(session: Session = Depends(get_db)):
    produtos = RepositorioProduto(session).listar()
    return produtos

@router.get('/produtos/{id}')
async def exibir_produto(id: int, session: Session = Depends(get_db)):
    produto = RepositorioProduto(session).buscarPorId(id)
    if not produto:
        raise HTTPException(status_code=404, detail='Não há um produto com este ID')

    return produto

@router.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=ProdutoSimples)
async def criar_produtos(produto: Produto, session: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(session).criar(produto)
    return produto_criado


@router.put('/produtos/{id}', response_model=ProdutoSimples)
async def atualizar_produto(id: int, produto: Produto, session: Session = Depends(get_db)):
    RepositorioProduto(session).editar(id, produto)
    produto.id = id
    return produto


@router.delete('/produtos/{id}')
async def remover_produto(id: int, session: Session = Depends(get_db)):
    RepositorioProduto(session).remover(id)
    return {'Mensagem': 'Produto Removido'}