from flask import Flask, request
import os
import psycopg2

app = Flask(__name__)

# Environment variables for DB connection
DB_HOST = os.environ.get('DB_HOST', 'db')
DB_USER = os.environ.get('DB_USER', 'user')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')
DB_NAME = os.environ.get('DB_NAME', 'mydb')

def get_conn():
    return psycopg2.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        dbname=DB_NAME
    )

@app.route("/")
def index():
    try:
        conn = get_conn()
        conn.close()
        return "Conexão com banco OK!\nCriado por: Daniel Coelho"
    except Exception as e:
        return f"Erro: {e}"

@app.route("/health")
def health():
    return {"status": "ok"}, 200

@app.route("/init")
def init_db():
    conn = get_conn()
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

@app.route("/users", methods=["GET"])
def get_users():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return {"users": users}

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    name = data.get("name")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name) VALUES (%s) RETURNING id;", (name,))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return {"id": user_id, "name": name}, 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
