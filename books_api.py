import requests
import sqlite3

def fetch_books(query="python", limit=10):
    url = f"https://openlibrary.org/search.json?q={query}&limit={limit}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        books = []
        for doc in data.get('docs', []):
            title = doc.get('title')
            author = doc.get('author_name', ['Unknown'])[0]
            year = doc.get('first_publish_year', None)
            books.append((title, author, year))
        return books
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return []

def setup_database():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            publication_year INTEGER
        )
    ''')
    # Clear existing data for a clean run
    cursor.execute('DELETE FROM books')
    conn.commit()
    return conn

def store_books(conn, books):
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO books (title, author, publication_year) VALUES (?, ?, ?)', books)
    conn.commit()
    print(f"Inserted {len(books)} books into the database.")

def display_books(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT title, author, publication_year FROM books')
    rows = cursor.fetchall()
    print("\n stored Books:")
    print("-" * 50)
    print(f"{'Title':<40} | {'Author':<20} | {'Year'}")
    print("-" * 50)
    for row in rows:
        title = row[0][:37] + "..." if len(row[0]) > 37 else row[0]
        author = row[1][:17] + "..." if len(row[1]) > 17 else row[1]
        year = row[2] if row[2] else "N/A"
        print(f"{title:<40} | {author:<20} | {year}")

def main():
    print("Fetching books from API...")
    books = fetch_books()
    if books:
        conn = setup_database()
        store_books(conn, books)
        display_books(conn)
        conn.close()
    else:
        print("No books found.")

if __name__ == "__main__":
    main()
