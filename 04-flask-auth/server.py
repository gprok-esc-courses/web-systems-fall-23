from flask import Flask, render_template, g, session, redirect, url_for, request

users = [
    {'username': 'admin', 'password': '1234', 'role': 'ADMIN', 'page': 'admin'},
    {'username': 'jdoe', 'password': '1111', 'role': 'USER', 'page': 'dashboard'},
]

app = Flask(__name__)
app.secret_key = 'asldkn8asd7aksjdhasd7asdkasdasdaksdg876a78sd87ads'
app.config['SESSION_TYPE'] = 'filesystem'

def check_loggedin_user():
    username = session.get("username")
    if username is None:
        g.user = None
    else:
        for u in users:
            if u['username'] == username:
                g.user = u 
                break

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for u in users:
            if u['username'] == username and u['password'] == password:
                # set the session
                session['username'] = username
                return redirect(url_for(u['page']))    
        return render_template("login.html", error="Wrong credentials")
    else:
        return render_template("login.html", error="")


@app.route("/dashboard")
def dashboard():
    check_loggedin_user()
    if g.user is None or g.user['role'] != 'USER':
        return redirect(url_for("login"))
    return render_template("dashboard.html")


@app.route("/admin")
def admin():
    check_loggedin_user()
    if g.user is None or g.user['role'] != 'ADMIN':
        return redirect(url_for("login"))
    return render_template("admin.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))