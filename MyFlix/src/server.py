from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.config.database import criar_db, get_db
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.series import RepositorioSerie

criar_db()

app = FastAPI()


@app.post('/series')
async def criar_serie(serie: schemas.Serie, db: Session = Depends(get_db)):
  serie_criada = RepositorioSerie(db).criar(serie)
  return serie_criada

@app.get('/series')
async def listar_serie(db: Session = Depends(get_db)):
  series = RepositorioSerie(db).listar()
  return series

@app.get('/series/{serie_id}')
async def obter_serie(serie_id: int, db: Session = Depends(get_db)):
  serie = RepositorioSerie(db).obter(serie_id)
  return serie

@app.delete('/series/{serie_id}')
async def obter_serie(serie_id: int, db: Session = Depends(get_db)):
  RepositorioSerie(db).remover(serie_id)
  return {"msg": "Removido com sucesso"}