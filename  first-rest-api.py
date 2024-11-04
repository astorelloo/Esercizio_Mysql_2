from flask import Flask, jsonify
import mysql.connector
import jason
import pymysql

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)
mycursor = mydb.cursor()

app = Flask(__name__)

def hello():
    return "Hello, World!"

def getAllData():
    mtcursor = mysql.connection.cursor()
    mycursor.execute("SELECT * FROM Mammiferi")
    rows = mycursor.fetchall()
    result = [];
    for x in myresult:
        print(x);
        result.append(x);
    return result

def getByRazza(razza): #nome del metodo(variabile interessata)
    query= " SELECT * FROM Mammiferi WHERE razza = %s"
    mycursor.execute(query,(razza))
    rows = mycursor.fetchall()

@app.route("/")
def index():
    data = getAllData()
    return jsonify({'Mammiferi': data})

@approute("/<razza>")
def Koala(razza):
    data = getByRazza(razza)
    return jsonify({razz: data})

if __name__ == "__main__":
    app.run()