import sqlite3

conn = sqlite3.connect('formats.db')
c = conn.cursor()

# Créer table
c.execute('''
CREATE TABLE formats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT,
    hook TEXT,
    script TEXT,
    duree TEXT,
    categorie TEXT
)
''')

# Ajouter quelques formats
formats = [
    ("Dilemme", "90% regrettent", "Pose un dilemme puis commentaire", "7-9s", "dilemme"),
    ("Quiz", "Seuls les intelligents", "Pose question puis réponse", "6-8s", "quiz")
]

c.executemany('INSERT INTO formats (titre, hook, script, duree, categorie) VALUES (?,?,?,?,?)', formats)

conn.commit()
conn.close()
