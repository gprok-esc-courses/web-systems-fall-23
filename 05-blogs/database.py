import sqlite3
import os
from models import User, Post
from hashlib import md5


def get_db_connection():
    con = sqlite3.connect('blogs.db')
    return con


def create_db():
    if not os.path.exists('blogs.db'):
        con = get_db_connection()
        con.close()

def create_tables():
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     username TEXT,
                     password TEXT,
                     role TEXT)
                    """)
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS posts 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    title TEXT, 
                    users_id INTEGER,
                    FOREIGN KEY(users_id) REFERENCES users(id))
                    """)
    con.commit()
    con.close()


def get_bloggers():
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users WHERE role='BLOGGER'")
    result = cursor.fetchall()
    bloggers = []
    for row in result:
        blogger = User(row[0], row[1], row[2], row[3])
        bloggers.append(blogger)
    return bloggers

def get_posts(bid):
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM posts WHERE users_id=?", (bid,))
    result = cursor.fetchall()
    posts = []
    for row in result:
        post = Post(row[0], row[1], row[2])
        posts.append(post)
    return posts

def get_blogger(bid):
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users WHERE id=?", (bid,))
    row = cursor.fetchone()
    blogger = User(row[0], row[1], row[2], row[3])
    return blogger

def get_user(username):
    con = get_db_connection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    row = cursor.fetchone()
    if row is not None:
        user = User(row[0], row[1], row[2], row[3])
        return user
    else:
        return None
    
def add_user(username, password):
    con = get_db_connection()
    cursor = con.cursor()
    print(hash(password))
    cursor.execute("INSERT INTO users(username, password, role) VALUES (?, ?, 'BLOGGER')", 
                   (username, password))
    con.commit()
