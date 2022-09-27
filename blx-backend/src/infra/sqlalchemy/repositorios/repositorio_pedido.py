from pyexpat import model
from sqlalchemy import update, delete, select
from sqlalchemy.orm import Session
from src.schema import schemas
from src.infra.sqlalchemy.models import models


class RepositorioPedido():

    def __init__(self, session: Session) -> None:
        self.session = session
        

    def criar(self, pedido: schemas.Pedido) -> models.Pedido:
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

    def buscar_por_id(self, id: int) -> models.Pedido:
        stmt = select(models.Pedido).where(models.Pedido.id == id)
        pedido = self.session.execute(stmt).first()
        return pedido

    def listar_meus_pedidos_por_usuario_id(self, usuario_id: int) -> list[models.Pedido]:
        pass

    def listar_minhas_vendas_por_usuario_id(self, usuario_id: int) -> list[models.Pedido]:
        pass

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
