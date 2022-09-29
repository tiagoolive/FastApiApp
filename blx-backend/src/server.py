from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers import rotas_produtos, rotas_auth, rotas_pedidos
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

# rotas PRODUTOS
app.include_router(rotas_produtos.router)


# rotas SEGURANÇA: Autenticação e Autorização
app.include_router(rotas_auth.router, prefix='/auth')


# rotas PEDIDOS
app.include_router(rotas_pedidos.router)

