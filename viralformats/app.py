import random
from flask import Flask, render_template

app = Flask(__name__)

# Liste initiale de formats
formats = [
    {"titre":"Dilemme", "hook":"90% regrettent", "script":"Pose un dilemme", "duree":"7-9s"},
    {"titre":"Quiz", "hook":"Seuls les intelligents", "script":"Pose une question", "duree":"6-8s"}
]

@app.route("/")
def index():
    return render_template("index.html", formats=formats)

@app.route("/generate")
def generate():
    f = random.choice(formats)
    return render_template("index.html", formats=[f])

if __name__ == "__main__":
    app.run(debug=True)
