from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models
from src.schemas import schemas

class RepositorioSerie():

  def __init__(self, db: Session):
    self.db = db

  def criar(self, serie: schemas.Serie):
    db_serie = models.Serie(
      titulo = serie.titulo,
      ano = serie.ano,
      genero = serie.genero,
      qtd_temporada = serie.qtd_temporadas
    )
    self.db.add(db_serie)
    self.db.commit()
    self.db.refresh(db_serie)

    return db_serie

  def listar(self):
    series = self.db.query(models.Serie).all()
    return series

  def obter(self):
    pass

  def remover(self):
    pass