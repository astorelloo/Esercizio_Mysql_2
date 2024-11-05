from flask import Flask, jsonify, request  # Added `request` import
import mysql.connector
import pymysql

# Connect to MySQL
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
    result = []
    for x in rows:
        result.append(x)
    return result

def getByRazza(razza):
    query = "SELECT * FROM Mammiferi WHERE razza = %s"
    mycursor.execute(query, (razza,))
    rows = mycursor.fetchall()
    return rows

def addMammifero(data):
    query = "INSERT INTO Mammiferi (razza, nome, peso, eta) VALUES (%s, %s, %s, %s)"
    values = (data['razza'], data['nome'], data['peso'], data['eta'])
    mycursor.execute(query, values)
    mydb.commit()
    return mycursor.rowcount  # Returns the number of rows inserted (should be 1)

@app.route("/")
def index():
    data = getAllData()
    return jsonify({'Mammiferi': data})

@app.route("/<razza>")
def Koala(razza):
    data = getByRazza(razza)
    return jsonify({razza: data})

@app.route("/add", methods=["POST"])  # Added POST method here
def add():
    # Get the JSON data from the request
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    # Check if all required fields are present in the data
    required_fields = ['razza', 'nome', 'peso', 'eta']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing fields in data'}), 400

    # Insert the data into the database
    rows_inserted = addMammifero(data)
    if rows_inserted == 1:
        return jsonify({'message': 'Mammifero added successfully'}), 201
    else:
        return jsonify({'error': 'Failed to add Mammifero'}), 500

if __name__ == "__main__":
    app.run()