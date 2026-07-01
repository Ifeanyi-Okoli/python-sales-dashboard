import sqlite3

from datetime import datetime

DATABASE = "database/analytics.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            upload_date TEXT NOT NULL,
            rows INTEGER NOT NULL,
            columns INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()

    


def save_analysis(filename, rows, columns):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO analyses
        (filename, upload_date, rows, columns)
        VALUES (?, ?, ?, ?)
        """,
        (
            filename,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            rows,
            columns,
        ),
    )

    conn.commit()
    conn.close()

def get_all_analyses():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            filename,
            upload_date,
            rows,
            columns
        FROM analyses
        ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data