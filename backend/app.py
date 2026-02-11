from flask import Flask
import os
import psycopg2

app = Flask(__name__)

# Conecta no banco usando variáveis de ambiente
DB_HOST = os.environ.get('DB_HOST', 'db')
DB_USER = os.environ.get('DB_USER', 'user')
DB_PASS = os.environ.get('DB_PASSWORD', 'password')
DB_NAME = os.environ.get('DB_NAME', 'mydb')

@app.route("/")
def index():
    try:
        conn = psycopg2.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, dbname=DB_NAME)
        return "Conexão com banco OK!"
    except Exception as e:
        return f"Erro: {e}"

@app.route("/health")
def health():
    return {"status": "ok"}, 200

@app.route("/init")
def init_db():
    conn = psycopg2.connect(...)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
    return "Tabela criada"

@app.route("/users")
def get_users():
    conn = psycopg2.connect(...)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return {"users": users}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
