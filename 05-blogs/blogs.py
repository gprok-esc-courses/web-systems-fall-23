from flask import Flask, render_template, session, g, request, redirect
from flask_bcrypt import Bcrypt
import database as db
from hashlib import md5

app = Flask(__name__)
# create session secret key
app.secret_key = "kdjfdlkjhfsdkjhfdskj56kjsdhdskjhfkjs"
app.config['SESSION_TYPE'] = 'filesystem'
bcrypt = Bcrypt(app) 

db.create_db()
db.create_tables()

def check_loggedin_user():
    username = session.get("username")
    if username is None:
        g.user = None
    else:
        g.user = db.get_user(username)

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

@app.route("/login", methods=['GET', 'POST'])
def login():
    check_loggedin_user()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = db.get_user(username)
        if user is None:
            return render_template("login.html", message="User not found")
        else:
            if bcrypt.check_password_hash(user.password, password):
                session["username"] = username
                return redirect("/")
            else:
                return render_template("login.html", message="Wrong password")      
    else:
        return render_template("login.html")
    
@app.route("/register", methods=['GET', 'POST'])
def register():
    check_loggedin_user()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        if password != password2:
            return render_template("register.html", message="Passwords do not match.")
        else:
            user = db.get_user(username)
            if user is not None:
                return render_template("register.html", message="Username already taken.")
            else:
                db.add_user(username, bcrypt.generate_password_hash(password).decode('utf-8'))
                return redirect("/login")
    else:
        return render_template("register.html")


@app.route("/logout")
def logout():
    session.pop("username")
    return redirect("/")