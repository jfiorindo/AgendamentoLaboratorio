from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()



app = Flask(__name__)
CORS(app)

# Configuração do banco
import mysql.connector
from mysql.connector import Error

try:
    db = mysql.connector.connect(
        host="localhost",
        user="Gabriell",
        password="Laboratorio#321",
        database="agendamento_lab"
    )
    if db.is_connected():
        print("Conectado ao banco de dados MySQL com sucesso!")
    cursor = db.cursor(dictionary=True)
except Error as e:
    print(f"Erro ao conectar ao MySQL: {e}")


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    nome = data["nome"]
    senha = data["senha"]

    cursor.execute("SELECT * FROM usuarios WHERE nome=%s AND senha=%s", (nome, senha))
    user = cursor.fetchone()

    if user:
        return jsonify({"mensagem": "Login bem-sucedido", "usuario_id": user["id"]})
    else:
        return jsonify({"mensagem": "Usuário ou senha incorretos"}), 401

@app.route("/agendar", methods=["POST"])
def agendar():
    data = request.get_json()
    usuario_id = data["usuario_id"]
    laboratorio = data["laboratorio"]
    data_agendada = data["data"]

    cursor.execute("INSERT INTO agendamentos (usuario_id, laboratorio, data) VALUES (%s, %s, %s)", 
                   (usuario_id, laboratorio, data_agendada))
    db.commit()
    return jsonify({"mensagem": "Agendamento realizado com sucesso!"})

@app.route("/agendamentos", methods=["GET"])
def listar_agendamentos():
    cursor.execute("SELECT * FROM agendamentos")
    agendamentos = cursor.fetchall()
    return jsonify(agendamentos)

if __name__ == "__main__":
    app.run(debug=True)
