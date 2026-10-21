
import os
import sqlite3
from pathlib import Path

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = Path(
    os.environ.get("APP_DB_PATH", str(BASE_DIR / "app.db"))
)

app = Flask(__name__)
app.config["DEBUG"] = False
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_db()
    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        """)

        count = conn.execute(
            "SELECT COUNT(*) FROM products"
        ).fetchone()[0]

        if count == 0:
            conn.executemany(
                "INSERT INTO products (name) VALUES (?)",
                [("Keyboard",), ("Mouse",), ("Monitor",)]
            )

        conn.commit()
    finally:
        conn.close()


@app.get("/")
def home():
    return jsonify({
        "project": "HorizonTechX Secure Coding Review",
        "status": "running",
        "endpoints": [
            "/health",
            "/search?q=mouse",
            "/register",
            "/login"
        ]
    })


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/search")
def search():
    query = request.args.get("q", "").strip()

    if not query or len(query) > 100:
        return jsonify({
            "error": "Query must be 1–100 characters"
        }), 400

    conn = get_db()
    try:
        rows = conn.execute(
            "SELECT id, name FROM products WHERE name LIKE ?",
            (f"%{query}%",)
        ).fetchall()

        results = [dict(row) for row in rows]
    finally:
        conn.close()

    return jsonify({"results": results})


@app.post("/register")
def register():
    data = request.get_json(silent=True) or {}
    username = data.get("username", "")
    password = data.get("password", "")

    if not isinstance(username, str) or not 3 <= len(username) <= 40:
        return jsonify({
            "error": "Username must be 3–40 characters"
        }), 400

    if not isinstance(password, str) or not 12 <= len(password) <= 128:
        return jsonify({
            "error": "Password must be 12–128 characters"
        }), 400

    password_hash = generate_password_hash(password)

    conn = get_db()
    try:
        conn.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, password_hash)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        return jsonify({
            "error": "Registration could not be completed"
        }), 409
    finally:
        conn.close()

    return jsonify({"message": "User registered"}), 201


@app.post("/login")
def login():
    data = request.get_json(silent=True) or {}
    username = data.get("username", "")
    password = data.get("password", "")

    if not isinstance(username, str) or not isinstance(password, str):
        return jsonify({
            "error": "Invalid username or password"
        }), 401

    if len(username) > 40 or len(password) > 128:
        return jsonify({
            "error": "Invalid username or password"
        }), 401

    conn = get_db()
    try:
        user = conn.execute(
            "SELECT password_hash FROM users WHERE username = ?",
            (username,)
        ).fetchone()
    finally:
        conn.close()

    if user is None or not check_password_hash(
        user["password_hash"], password
    ):
        return jsonify({
            "error": "Invalid username or password"
        }), 401

    return jsonify({"message": "Login successful"})


if __name__ == "__main__":
    init_db()
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )

