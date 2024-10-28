#attraverso python facciamo degli inserimenti
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Database_Astor"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Compagni (nome, cognome) VALUES (%s, %s)"
val = ("antonio", "soliman ")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserto.")