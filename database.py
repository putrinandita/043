import sqlite3

def connect():
    return sqlite3.connect("perpustakaan.db")

def setup():
    conn = connect()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS buku (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            judul TEXT,
            penulis TEXT,
            kategori TEXT
        )
    ''')
    conn.commit()
    conn.close()
