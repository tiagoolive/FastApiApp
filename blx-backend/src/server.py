from fastapi import FastAPI, Depends, status
from src.schema.schemas import Produto, Usuario, ProdutoSimples
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.usuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_db, criar_db

# criar_db()

app = FastAPI()

# PRODUTOS

@app.get('/produtos', response_model=list[Produto])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos


@app.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=ProdutoSimples)
async def criar_produtos(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado
    
# USUARIOS 

@app.get('/usuarios')
async def listar_usuarios(db: Session = Depends(get_db), response_model = list[Usuario]):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios


@app.post('/usuarios')
async def criar_usuarios(usuario: Usuario, db: Session = Depends(get_db), status_code=status.HTTP_201_CREATED, response_model = Usuario):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado
