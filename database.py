import sqlite3

def init_db():
    conn = sqlite3.connect("incidents.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incident_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            issue TEXT,
            category TEXT,
            automation_result TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def log_incident(issue: str, category: str, automation_result: str):
    conn = sqlite3.connect("incidents.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO incident_logs (issue, category, automation_result)
        VALUES (?, ?, ?)
    """, (issue, category, automation_result))

    conn.commit()
    conn.close()
