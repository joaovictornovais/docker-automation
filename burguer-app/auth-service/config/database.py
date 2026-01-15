# Conecta ao  banco de dados MongoDB utilizando as variáveis de ambiente

from pymongo import MongoClient
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

# Carrega as variáveis de ambiente do arquivo .env

load_dotenv()

#Processa a URI do MongoDB para escapar caracteres especiais na senha
mongo_uri = os.getenv("MONGO_URI")
if mongo_uri:
    user_info, rest = mongo_uri.split("@", 1)
    if ":" in user_info:
        username, password = user_info.split(":", 1)
        password = quote_plus(password)
        mongo_uri = f"{username}:{password}@{rest}"

#Cria a conexão com o banco de dados MongoDB

client = MongoClient(mongo_uri)

# Seleciona o banco de dados
db = client["burguer_app_db"]

# função para retornar a instância do banco de dados
def get_db():
    return db
