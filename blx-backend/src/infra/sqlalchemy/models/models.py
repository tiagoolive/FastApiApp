from sqlalchemy import Column, Integer, String, Float, Boolean
from ..config.database import Base

class Produto(Base):
  __tablename__ = 'produto'

  id = Column(Integer, primary_key=True, index=True)
  nome = Column(String)
  detalhes = Column(String)
  preco = Column(Float)
  disponivel = Column(Boolean)
  tamanhos = Column(String)

class Usuario(Base):
  __tablename__ = 'usuario'

  id = Column(Integer, primary_key=True, index=True)
  nome = Column(String)
  telefone = Column(String)