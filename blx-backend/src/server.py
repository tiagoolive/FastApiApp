from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from src.schema.schemas import Produto, Usuario, ProdutoSimples
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_db, criar_db

# criar_db()

app = FastAPI()

# CORS
origins = [
    'http://localhost:3000',
    'https://localhost'
]
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )

# PRODUTOS


@app.get('/produtos', response_model=list[Produto])
def listar_produtos(session: Session = Depends(get_db)):
    produtos = RepositorioProduto(session).listar()
    return produtos


@app.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=ProdutoSimples)
async def criar_produtos(produto: Produto, session: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(session).criar(produto)
    return produto_criado


@app.put('/produtos/{id}', response_model=ProdutoSimples)
async def atualizar_produto(id: int, produto: Produto, session: Session = Depends(get_db)):
    RepositorioProduto(session).editar(id, produto)
    produto.id = id
    return produto


@app.delete('/produtos/{id}')
async def remover_produto(id: int, session: Session = Depends(get_db)):
    RepositorioProduto(session).remover(id)
    return {'Mensagem': 'Produto Removido'}

# USUARIOS


@app.get('/usuarios')
async def listar_usuarios(session: Session = Depends(get_db), response_model=list[Usuario]):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios


@app.post('/signup')
async def signup(usuario: Usuario, session: Session = Depends(get_db), status_code=status.HTTP_201_CREATED, response_model=Usuario):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado
