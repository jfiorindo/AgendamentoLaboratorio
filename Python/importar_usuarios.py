import json
from pymongo import MongoClient

# Conexão com o MongoDB local
client = MongoClient("mongodb://localhost:27017")
db = client["agendamento_lab"]
usuarios_collection = db["usuarios"]

# Carregar o arquivo usuarios.json
with open("usuarios.json", "r", encoding="utf-8") as f:
    usuarios = json.load(f)

# Inserir no banco
usuarios_collection.insert_many(usuarios)
print("Usuários inseridos com sucesso!")
