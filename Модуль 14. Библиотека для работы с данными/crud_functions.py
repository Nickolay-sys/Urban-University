import sqlite3

def initiate_db():
    con = sqlite3.connect("prod_db.db")
    cur = con.cursor()
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
    con.commit()
    con.close()

def get_all_products():
    con = sqlite3.connect("prod_db.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Products")
    products = cur.fetchall()
    for product in products:
        id, title, description, price = product
        print(f"Название: {title} | Описание: {description} | Цена: {price}")
    con.close()
    return products

if __name__ == "__main__":
    initiate_db()