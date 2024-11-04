import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "Animali"
)
mycursor = mydb.cursor()
sql = "INSERT INTO Mammiferi (nome, razza, peso, eta) VALUES ( %s, %s, %s, %s)"
animali = [
    ("Leo", "Leone africano", 190, 8),
    ("Bella", "Golden Retriever", 30, 5),
    ("Max", " Elefante africano", 5000, 25),
    ("Mia", "Cavallo purosangue", 500, 7),
    ("Oliver", "Koala", 8, 4)
]
mycursor.executemany(sql, animali)
print(mycursor.rowcount, "i record sono stati inseriti")
# Conferma le modifiche al database
mydb.commit()


