import sqlite3

con = sqlite3.connect("bot_db.db")
cur = con.cursor()

def initiate_db():
    cur.execute('''
                CREATE TABLE IF NOT EXISTS Products(
                    product_id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    description TEXT,
                    price INTEGER NOT NULL
                )
                ''')
    for i in range(1,5):
        cur.execute("INSERT INTO Products(product_id, title, description, price) VALUES (?, ?, ?, ?)",
                    (i,f"Название {i} ", f"Описание {i} ", f"{i*100}"))
    
    cur.execute('''
                CREATE TABLE IF NOT EXISTS Users(
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    balance INTEGER NOT NULL
                )
                ''')
    con.commit()

def get_all_products():
    cur.execute("SELECT * FROM Products")
    products = cur.fetchall()
    for product in products:
        id, title, description, price = product
        print(f"Название: {title} | Описание: {description} | Цена: {price}")
    return products

def add_user(username, email, age, balance=1000):
    cur.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)',
                (username, email, age, balance))
    con.commit()
    
def is_included(username):
    if cur.execute("SELECT COUNT(*) FROM Users WHERE username = ?",
                   (username,)).fetchone()[0]:
        return True
    else:
        False
    
 
if __name__ == "__main__":
    initiate_db()