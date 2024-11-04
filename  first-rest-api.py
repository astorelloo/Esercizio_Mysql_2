from flask import Flask, jsonify # nella CLI: pip install flask 
import mysql.connector
import json
import pymysql #nella CLI pip install pymysql

#Connect to mysql
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="Animali"
)
mycursor = mydb.cursor()
app = Flask(__name__)

def getAllData():
    mycursor.execute("SELECT * FROM Mammiferi")
    rows = mycursor.fetchall()
    result = [];
    for x in rows:
        print(x);
        result.append(x);
    return result

def getByRazza(razza): #nome del metodo(variabile interessata)
    query= " SELECT * FROM Mammiferi WHERE razza = %s"
    mycursor.execute(query,(razza,)) #attenzione alla virgola doopo (razza,)
    rows = mycursor.fetchall()
    return rows

@app.route("/")
def index():
    data = getAllData()
    return jsonify({'Mammiferi': data})

@app.route("/<razza>")
def Koala(razza):
    data = getByRazza(razza)
    return jsonify({razza: data})

if __name__ == "__main__":
    app.run()