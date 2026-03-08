from flask import Flask, render_template

app = Flask(__name__)

formats = [
    {
        "titre": "Dilemme viral",
        "hook": "90% des gens regrettent leur réponse.",
        "script": "Pose un dilemme puis demande la réponse en commentaire.",
        "duree": "7-9 secondes"
    },
    {
        "titre": "Quiz impossible",
        "hook": "Seuls les gens intelligents trouvent.",
        "script": "Pose une question puis révèle la réponse.",
        "duree": "6-8 secondes"
    }
]

@app.route("/")
def index():
    return render_template("index.html", formats=formats)

if __name__ == "__main__":
    app.run(debug=True)