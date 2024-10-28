#in questo file si crea una tabella
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Database_Astor"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Compagni (nome VARCHAR(255), cognome VARCHAR(255))")