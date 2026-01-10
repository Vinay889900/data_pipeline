import csv
import sqlite3
import os

def setup_database(db_name='users.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE
        )
    ''')
    # Clear existing data for a clean run
    cursor.execute('DELETE FROM users')
    conn.commit()
    return conn

def import_csv_to_db(csv_file, db_name='users.db'):
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found.")
        return

    conn = setup_database(db_name)
    cursor = conn.cursor()

    try:
        with open(csv_file, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            users = []
            for row in reader:
                name = row.get('Name')
                email = row.get('Email')
                if name and email:
                    users.append((name, email))
            
            if users:
                cursor.executemany('INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)', users)
                conn.commit()
                print(f"Successfully imported {len(users)} users into {db_name}.")
            else:
                print("No valid data found in CSV.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

def verify_import(db_name='users.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    print("\nImported Users:")
    print("-" * 40)
    print(f"{'ID':<5} | {'Name':<20} | {'Email'}")
    print("-" * 40)
    for row in rows:
        print(f"{row[0]:<5} | {row[1]:<20} | {row[2]}")
    conn.close()

def main():
    csv_file = 'users.csv'
    print(f"Importing data from {csv_file}...")
    import_csv_to_db(csv_file)
    verify_import()

if __name__ == "__main__":
    main()
