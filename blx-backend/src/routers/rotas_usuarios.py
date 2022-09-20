from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.config.database import get_db
from src.schema.schemas import Usuario
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario

router = APIRouter()


@router.get('/usuarios')
async def listar_usuarios(session: Session = Depends(get_db), response_model=list[Usuario]):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios


@router.post('/signup')
async def signup(usuario: Usuario, session: Session = Depends(get_db), status_code=status.HTTP_201_CREATED, response_model=Usuario):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado
