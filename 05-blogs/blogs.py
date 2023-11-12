from flask import Flask, render_template, session, g
from flask_bcrypt import Bcrypt
import database as db

app = Flask(__name__)
bcrypt = Bcrypt(app) 

db.create_db()
db.create_tables()

def check_loggedin_user():
    username = session.get("username")
    if username is None:
        g.user = None
    else:
        g.user = None
        # for u in users:
        #     if u['username'] == username:
        #         g.user = u 
        #         break

@app.route("/")
def home():
    check_loggedin_user()
    return render_template("home.html", user=g.user)

@app.route("/about")
def about():
    check_loggedin_user()
    return render_template("about.html", user=g.user)

@app.route("/bloggers")
def bloggers():
    check_loggedin_user()
    bloggers = db.get_bloggers()
    return render_template("bloggers.html", user=g.user, bloggers=bloggers)

@app.route("/posts/<bid>")
def posts(bid):
    check_loggedin_user()
    blogger = db.get_blogger(bid)
    posts = db.get_posts(bid)
    return render_template("posts.html", user=g.user, blogger=blogger, posts=posts)
