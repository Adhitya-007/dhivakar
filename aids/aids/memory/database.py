import sqlite3
import json

DB_NAME = "traffic_game.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS world_state (
        id INTEGER PRIMARY KEY,
        state TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS strategies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        action TEXT,
        efficiency REAL
    )
    """)

    conn.commit()
    conn.close()


def save_world(state):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM world_state")
    cursor.execute(
        "INSERT INTO world_state (id, state) VALUES (?, ?)",
        (1, json.dumps(state))
    )

    conn.commit()
    conn.close()


def load_world():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT state FROM world_state WHERE id=1")
    row = cursor.fetchone()
    conn.close()

    if row:
        return json.loads(row[0])
    return None


def store_strategy(action, efficiency):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO strategies (action, efficiency) VALUES (?, ?)",
        (json.dumps(action), efficiency)
    )

    conn.commit()
    conn.close()


def get_best_strategy():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT action FROM strategies ORDER BY efficiency DESC LIMIT 1"
    )
    row = cursor.fetchone()
    conn.close()

    if row:
        return json.loads(row[0])
    return None