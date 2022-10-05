from datetime import datetime, timedelta
from jose import jwt

# CONFIG
SECRET_KEY = '698dc19d489c4e4db73e28a713eab07b'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 3000

def criar_acess_token(data: dict):
  dados = data.copy()
  expiracao = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)

  dados.update({'exp': expiracao})

  token_jwt = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
  return token_jwt


def verificar_acess_token(token: str):
  payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
  return payload.get('sub')