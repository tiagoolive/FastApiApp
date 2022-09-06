from fastapi import FastAPI, Depends
from src.schema import schemas
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_db, criar_db

criar_db()

app = FastAPI()


@app.get('/produtos')
async def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos


@app.post('/produtos')
async def criar_produtos(produto: schemas.Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get('/usuarios')
async def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios


@app.post('/usuarios')
async def criar_usuarios(usuario: schemas.Usuario, db: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado
