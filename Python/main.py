from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
CORS(app)

# Conecta ao MongoDB local
client = MongoClient("mongodb://localhost:27017")
db = client["agendamento_lab"]
usuarios_collection = db["usuarios"]

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    print("Recebido:", data)  # 🔍 veja o que o JS está mandando

    nome = data.get("nome")
    senha = data.get("senha")

    usuario = usuarios_collection.find_one({"nome": nome, "senha": senha})
    print("Usuário encontrado:", usuario)  # 🔍 veja se achou

    if usuario:
        return jsonify({
            "mensagem": "Login bem-sucedido",
            "usuario_id": str(usuario["_id"]),
            "nome": usuario["nome"]
        })
    else:
        return jsonify({"mensagem": "Usuário ou senha incorretos"}), 401
if __name__ == "__main__":
    app.run(debug=True)
