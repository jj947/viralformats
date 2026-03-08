import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
