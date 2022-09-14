from sqlalchemy import update, delete
from sqlalchemy.orm import Session
from src.schema import schemas
from src.infra.sqlalchemy.models import models


class RepositorioProduto():

    def __init__(self, session: Session):
        self.session = session

    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(
            nome=produto.nome,
            detalhes=produto.detalhes,
            preco=produto.preco,
            disponivel=produto.disponivel,
            usuario_id=produto.usuario_id
        )
        self.session.add(db_produto)
        self.session.commit()
        self.session.refresh(db_produto)
        return db_produto

    def listar(self):
        produtos = self.session.query(models.Produto).all()
        return produtos

    def editar(self, produto: schemas.Produto):
        stmt = update(models.Produto).where(models.Produto.id == produto.id).values(
            nome=produto.nome,
            detalhes=produto.detalhes,
            preco=produto.preco,
            disponivel=produto.disponivel
        )
        self.session.execute(stmt)
        self.session.commit()

    def remover(self, id: int):
        stmt = delete(models.Produto).where(models.Produto.id == id)
        self.session.execute(stmt)
        self.session.commit()
