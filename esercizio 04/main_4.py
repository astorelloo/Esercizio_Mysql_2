#attraverso questo codice si fa la "select from"
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Database_Astor"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Compagni")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)