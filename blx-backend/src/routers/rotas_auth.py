from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.config.database import get_db
from src.schema.schemas import Usuario
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.providers import hash_provider

router = APIRouter()


@router.get('/usuarios')
async def listar_usuarios(session: Session = Depends(get_db), response_model=list[Usuario]):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios


@router.post('/signup')
async def signup(usuario: Usuario, session: Session = Depends(get_db), status_code=status.HTTP_201_CREATED, response_model=Usuario):
    # verificar se já existe um telefone
    usuario_localizado = RepositorioUsuario(
        session).obter_por_telefone(usuario.telefone)
        
    if (usuario_localizado):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Já existe um usuário para este telefone')

    # criar novo usuario
    usuario.senha = hash_provider.gerar_hash(usuario.senha)
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado