from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
CORS(app)

# Conexão com MongoDB local
client = MongoClient("mongodb://localhost:27017")
db = client["AgendamentoLaboratorio"]
usuarios_collection = db["usuarios"]

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    print("🔎 Recebido do front-end:", data)

    nome = str(data.get("nome", "")).strip()
    senha = str(data.get("senha", "")).strip()

    usuario = usuarios_collection.find_one({
        "nome": nome,
        "senha": senha
    })

    print("🔍 Resultado da busca:", usuario)

    if usuario:
        return jsonify({
            "mensagem": "Login bem-sucedido",
            "usuario_id": str(usuario["_id"]),
            "nome": usuario["nome"]
        }), 200
    else:
        return jsonify({"mensagem": "Usuário ou senha incorretos"}), 401

if __name__ == "__main__":
    app.run(debug=True)
