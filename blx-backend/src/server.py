from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers import rotas_produtos, rotas_usuarios, rotas_pedidos
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
app.include_router(rotas_produtos.router)


# USUARIOS
app.include_router(rotas_usuarios.router)


# PEDIDOS
app.include_router(rotas_pedidos.router)

