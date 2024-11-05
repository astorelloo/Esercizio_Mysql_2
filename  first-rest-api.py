from flask import Flask, jsonify, request
import mysql.connector
import pymysql

# Connessione a MySQL
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
    return mycursor.rowcount

@app.route("/")
def index():
    data = getAllData()
    return jsonify({'Mammiferi': data})

@app.route("/<razza>")
def getMammiferoByRazza(razza):
    data = getByRazza(razza)
    return jsonify({razza: data})

@app.route("/add", methods=["POST"])
def add():
    data = request.json
    if not data:
        return jsonify({'message': 'Nessun dato fornito'}), 400

    required_fields = ['razza', 'nome', 'peso', 'eta']
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Dati mancanti o errati'}), 400

    rows_inserted = addMammifero(data)
    if rows_inserted == 1:
        return jsonify({'message': 'Mammifero inserito con successo'}), 201
    else:
        return jsonify({'message': 'Errore durante l inserimento'}), 500

#-----------------------------------------------------------------------------
#da qua non va
        
def updateMammifero(id, data):
    query = "UPDATE Mammiferi SET nome = %s, razza = %s, peso = %s, eta = %s WHERE id = %s"
    values = (data['nome'], data['razza'], data['peso'], data['eta'], id)
    mycursor.execute(query, values)
    mydb.commit()
    return mycursor.rowcount

def deleteMammifero(id):
    query = "DELETE FROM Mammiferi WHERE id = %s"
    mycursor.execute(query, (id,))
    mydb.commit()
    return mycursor.rowcount

@app.route("/update/<id>", methods=["PUT"])
def update(id):
    data = request.json
    required_fields = ['nome', 'razza', 'peso', 'eta']
    if not all(field in data for field in required_fields):
        return jsonify({'message': 'Dati mancanti'}), 400

    rows_updated = updateMammifero(id, data)
    if rows_updated == 1:
        return jsonify({'message': 'Mammifero aggiornato con successo'}), 200
    else:
        return jsonify({'message': 'Errore durante l aggiornamento o ID non trovato'}), 404

@app.route("/delete/<id>", methods=["DELETE"])
def delete(id):
    rows_deleted = deleteMammifero(id)
    if rows_deleted == 1:
        return jsonify({'message': 'Mammifero eliminato con successo'}), 200
    else:
        return jsonify({'message': 'Errore durante l\'eliminazione o ID non trovato'}), 404

if __name__ == "__main__":
    app.run()