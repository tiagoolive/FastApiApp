from datetime import datetime, timedelta
from jose import jwt

# CONFIG
SECRET_KEY = '698dc19d489c4e4db73e28a713eab07b'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 3000

def criar_acess_token(data: dict):
  return 'token12345'


def verificar_acess_token(token: str):
  return '6194394837'