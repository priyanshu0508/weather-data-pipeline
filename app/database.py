import sqlite3
from config import DATABASE_NAME

def get_connection():
    return sqlite3.connect(DATABASE_NAME)

def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS weather_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_id INTEGER,
        temperature REAL,
        humidity INTEGER,
        pressure INTEGER,
        description TEXT,
        timestamp TEXT,
        FOREIGN KEY(city_id) REFERENCES cities(id)
    )
    """)

    conn.commit()
    conn.close()

def get_or_create_city(city):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM cities WHERE name=?", (city,))
    row = cur.fetchone()

    if row:
        city_id = row[0]
    else:
        cur.execute("INSERT INTO cities (name) VALUES (?)", (city,))
        conn.commit()
        city_id = cur.lastrowid

    conn.close()
    return city_id
