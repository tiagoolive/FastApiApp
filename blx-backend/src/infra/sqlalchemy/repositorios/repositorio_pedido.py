from sqlalchemy import update, delete, select
from sqlalchemy.orm import Session
from src.schema import schemas
from src.infra.sqlalchemy.models import models


class RepositorioPedido():

    def __init__(self, session: Session):
        self.session = session

    def criar(self, pedido: schemas.Pedido):
        db_pedido = models.Pedido(
            quantidade = pedido.quantidade,
            local_entrega = pedido.local_entrega,
            tipo_entrega = pedido.tipo_entrega,
            usuario_id = pedido.usuario_id,
            produto_id = pedido.produto_id,
            observacao = pedido.observacao
        )
        self.session.add(db_pedido)
        self.session.commit()
        self.session.refresh(db_pedido)
        return db_pedido

    def listar(self):
        pedidos = self.session.query(models.Pedido).all()
        return pedidos

    def buscarPorId(self, id: int):
        stmt = select(models.Pedido).where(models.Pedido.id == id)
        pedido = self.session.execute(stmt).first()
        return pedido

    def editar(self, id: int, pedido: schemas.Pedido):
        stmt = update(models.Pedido).where(models.Pedido.id == id).values(
            quantidade = pedido.quantidade,
            local_entrega = pedido.local_entrega,
            tipo_entrega = pedido.tipo_entrega,
            usuario_id = pedido.usuario_id,
            produto_id = pedido.produto_id,
            observacao = pedido.observacao
        )
        self.session.execute(stmt)
        self.session.commit()

    def remover(self, id: int):
        stmt = delete(models.Pedido).where(models.Pedido.id == id)
        self.session.execute(stmt)
        self.session.commit()
