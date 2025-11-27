from flask import Flask, request, jsonify
import sqlite3
import re

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return jsonify({"message": "API"})

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return jsonify([dict(user) for user in users])

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    conn = get_db()
    conn.execute('INSERT INTO users (name, email) VALUES (?, ?)', 
                (data['name'], data['email']))
    conn.commit()
    conn.close()
    return jsonify({"message": "User created"}), 201

@app.route('/search')
def search():
    query = request.args.get('q', '')
    conn = get_db()
    users = conn.execute(f"SELECT * FROM users WHERE name LIKE '%{query}%'").fetchall()
    conn.close()
    return jsonify([dict(user) for user in users])

if __name__ == '__main__':
    app.run(debug=True)
