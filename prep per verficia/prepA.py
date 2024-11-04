import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()
#creazione database con controllo se esite gia' (se c'e' non la crea)
mycursor.execute("CREATE DATABASE IF NOT EXISTS Animali")

#!!! da cambiare il mycursor e il mydb a seconda se si entra in un nuovo database!!!
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "Animali"#!!!!!
)
mycursor = mydb.cursor()
#creazione tabella mammiferi con controllo se esiste gia' (se c'e' non la crea)
mycursor.execute("CREATE TABLE IF NOT EXISTS Mammiferi (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, nome VARCHAR(255), razza VARCHAR(255), peso INT, eta INT)")

