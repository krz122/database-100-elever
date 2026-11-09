
import sqlite3

database = sqlite3.connect("elever.db")
cursor = database.cursor()

cursor.execute("DROP TABLE IF EXISTS elever")

cursor.execute("""
CREATE TABLE elever (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fornavn TEXT,
    etternavn TEXT,
    email TEXT,
    fodselsnummer TEXT,
    klasse TEXT
)
""")

fornavn = ["Emil", "Noah", "Emma", "Nora", "Oliver",
           "Lucas", "Sofie", "Maja", "Jakob", "Ella"]

etternavn = ["Hansen", "Olsen", "Johansen", "Larsen",
             "Berg", "Nilsen", "Dahl", "Moen"]

klasser = ["im1", "im2", "st1", "st2", "st3", "ho1", "ho2"]

for i in range(100):
    navn = fornavn[i % 10]
    etter = etternavn[i % 8]
    klasse = klasser[i % 7]

    email = navn.lower() + "." + etter.lower() + str(i + 1) + "@kvn.no"

    fodselsnummer = str(20070101 + i)

    cursor.execute("""
    INSERT INTO elever (fornavn, etternavn, email, fodselsnummer, klasse)
    VALUES (?, ?, ?, ?, ?)
    """, (navn, etter, email, fodselsnummer, klasse))

database.commit()

cursor.execute("SELECT * FROM elever")
elever = cursor.fetchall()

for elev in elever:
    print(elev)

print("Antall elever:", len(elever))

database.close()
