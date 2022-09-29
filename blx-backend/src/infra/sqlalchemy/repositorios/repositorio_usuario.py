from sqlalchemy import select
from sqlalchemy.orm import Session
from src.schema import schemas
from src.infra.sqlalchemy.models import models

class RepositorioUsuario():

  def __init__(self, db: Session):
    self.session = db

  def criar(self, usuario: schemas.Usuario):
    db_usuario = models.Usuario(
      nome = usuario.nome,
      senha = usuario.senha,
      telefone = usuario.telefone
    )
    self.session.add(db_usuario)
    self.session.commit()
    self.session.refresh(db_usuario)
    return db_usuario

  def listar(self):
    stmt = select(models.Usuario)
    usuarios = self.session.execute(stmt).scalars().all()
    return usuarios

  def obter_por_telefone(self, telefone):
    query = select(models.Usuario).where(models.Usuario.telefone == telefone)
    return self.session.execute(query).scalars().first()

  def remover():
    pass
    