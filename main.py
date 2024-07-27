import sqlite3
from sqlite3 import Error

def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        print("База данных подключена")
    except Error as e:
        print(e)
    return conn

def create_table(conn):
    try:
        sql = '''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_title TEXT NOT NULL,
            price REAL NOT NULL DEFAULT 0.0,
            quantity INTEGER NOT NULL DEFAULT 0
        )
        '''
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    except Error as e:
        print(e)

def add_products(conn):
    products = [
        ("Product1", 10.00, 20),
        ("Product2", 15.50, 30),
        ("Product3", 7.99, 10),
        ("Product4", 12.00, 25),
        ("Product5", 20.99, 15),
        ("Product6", 5.49, 40),
        ("Product7", 9.99, 22),
        ("Product8", 14.99, 17),
        ("Product9", 8.49, 33),
        ("Product10", 19.99, 10),
        ("Product11", 11.50, 28),
        ("Product12", 16.00, 12),
        ("Product13", 22.99, 7),
        ("Product14", 13.49, 19),
        ("Product15", 6.99, 45)
    ]
    try:
        sql = '''INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.executemany(sql, products)
        conn.commit()
    except Error as e:
        print(e)

def update_quantity(conn, product_id, quantity):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (quantity, product_id))
        conn.commit()
    except Error as e:
        print(e)

def update_price(conn, product_id, price):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (price, product_id))
        conn.commit()
    except Error as e:
        print(e)

def delete_product(conn, product_id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (product_id,))
        conn.commit()
    except Error as e:
        print(e)

def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)

def select_products_below_price_and_quantity(conn, price_limit, quantity_limit):
    try:
        sql = '''SELECT * FROM products WHERE price < ? AND quantity > ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (price_limit, quantity_limit))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)

def search_products_by_title(conn, search_term):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        cursor = conn.cursor()
        cursor.execute(sql, ('%' + search_term + '%',))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)

# Основной код
def main():
    db_name = "hw.db"
    connection = create_connection(db_name)

    if connection:
        create_table(connection)
        add_products(connection)

        # Пример использования функций
        print("Все товары:")
        select_all_products(connection)

        print("\nОбновляем количество товара с id 1 на 50")
        update_quantity(connection, 1, 50)

        print("\nОбновляем цену товара с id 2 на 25.00")
        update_price(connection, 2, 25.00)

        print("\nУдаляем товар с id 3")
        delete_product(connection, 3)

        print("\nТовары дешевле 100 и количество больше 5:")
        select_products_below_price_and_quantity(connection, 100, 5)

        print("\nПоиск товаров по названию 'Product12':")
        search_products_by_title(connection, 'Product12')

        connection.close()

if __name__ == '__main__':
    main()
