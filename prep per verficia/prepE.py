import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "Animali"
)
mycursor = mydb.cursor()

##programma che fa visualizzare gli animali con peso >2 
mycursor.execute("SELECT * FROM Mammiferi WHERE peso >= 2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)