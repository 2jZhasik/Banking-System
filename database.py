import sqlite3

def init_db():
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS clients (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        balance REAL DEFAULT 0.0
                    )''')
    conn.commit()
    conn.close()

def register_client(name):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clients (name, balance) VALUES (?, ?)", (name, 0.0))
    conn.commit()
    conn.close()
    return "Client registered successfully!"

def get_balance(client_id):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM clients WHERE id = ?", (client_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def deposit_money(client_id, amount):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE clients SET balance = balance + ? WHERE id = ?", (amount, client_id))
    conn.commit()
    conn.close()
    return "Deposit successful!"

def withdraw_money(client_id, amount):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM clients WHERE id = ?", (client_id,))
    result = cursor.fetchone()
    if result and result[0] >= amount:
        cursor.execute("UPDATE clients SET balance = balance - ? WHERE id = ?", (amount, client_id))
        conn.commit()
        conn.close()
        return "Withdrawal successful!"
    conn.close()
    return "Insufficient funds or client not found"

if __name__ == "__main__":
    init_db()
