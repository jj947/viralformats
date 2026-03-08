import random
import sqlite3
from flask import Flask, render_template
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
app = Flask(__name__)
# Liste initiale de formats
formats = [
    {"titre":"Dilemme", "hook":"90% regrettent", "script":"Pose un dilemme", "duree":"7-9s"},
    {"titre":"Quiz", "hook":"Seuls les intelligents", "script":"Pose une question", "duree":"6-8s"}
]
def get_formats():
    conn = sqlite3.connect('formats.db')
    c = conn.cursor()
    c.execute("SELECT titre, hook, script, duree, categorie FROM formats")
    formats = [{"titre": t, "hook": h, "script": s, "duree": d, "categorie": cat} for t,h,s,d,cat in c.fetchall()]
    conn.close()
    return formats

@app.route("/")
def index():
    formats = get_formats()
    return render_template("index.html", formats=formats)

@app.route("/generate")
def generate():
    formats = get_formats()
    import random
    f = random.choice(formats)
    return render_template("index.html", formats=[f])
login_manager = LoginManager()
login_manager.init_app(app)

# Utilisateur exemple
class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

# Base utilisateur temporaire
users = {"test": User(1, "test", "mdp")}

@login_manager.user_loader
def load_user(user_id):
    for user in users.values():
        if user.id == int(user_id):
            return user
    return None

@app.route("/login", methods=["GET","POST"])
def login():
    # ici tu peux mettre un formulaire HTML pour username/mdp
    # puis vérifier et faire login_user(user)
    pass

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return "Déconnecté"
if __name__ == "__main__":
    app.run(debug=True)


