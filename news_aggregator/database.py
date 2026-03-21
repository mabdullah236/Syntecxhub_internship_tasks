import sqlite3

def setup_db():
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS news 
                    (title TEXT UNIQUE, source TEXT, date TEXT, url TEXT)''')
    conn.commit()
    conn.close()

def save_news(articles):
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()
    for art in articles:
        try:
            cursor.execute("INSERT INTO news VALUES (?, ?, ?, ?)", 
                        (art['title'], art['source']['name'], art['publishedAt'], art['url']))
        except sqlite3.IntegrityError:
            continue 
    conn.commit()
    conn.close()

def get_filtered_news(source=None, keyword=None):
    conn = sqlite3.connect('news.db')
    query = "SELECT * FROM news WHERE 1=1"
    params = []
    
    if source:
        query += " AND source LIKE ?"
        params.append(f"%{source}%")
    if keyword:
        query += " AND title LIKE ?"
        params.append(f"%{keyword}%")
        
    cursor = conn.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return rows