import sqlite3
import os
from models import Product


def get_db_connection():
    con = sqlite3.connect('eshop.db')
    return con


def create_db():
    if not os.path.exists('eshop.db'):
        con = get_db_connection()
        cursor = con.cursor()
        cursor.execute("""
                       CREATE TABLE products 
                       (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        name TEXT, 
                        price NUMERIC)
                       """)
        con.commit()
        con.close()


def get_product(pid):
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM products WHERE id=?", (pid, ))
    result = cursor.fetchone()
    product = Product(result[0], result[1], result[2])
    print(product)
    return product


def get_all_products():
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM products")
    result = cursor.fetchall()
    products = []
    for row in result:
        product = Product(row[0], row[1], row[2])
        products.append(product)
    return products


def add_product(name, price):
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("INSERT INTO products (name, price) VALUES(?, ?)", (name, price))
    con.commit()
    con.close()