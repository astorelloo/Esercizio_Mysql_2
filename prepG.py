import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "Animali"
)
mycursor = mydb.cursor()
risp = input("Premi: 1) per per inserire un nuovo animale; 2) per visualizzare tutti gli animali; 3)per eliminare un animale, 4)per modificare un animale")
match risp:
    case 1:
       #1) per per inserire un nuovo animale
        nome = input("Inserisci il nome dell'animale: ")
        razza = input("Inserisci la razza dell'animale: ")
        
        while True:
            # Verifica se il peso è un intero
            peso_input = input("Inserisci il peso dell'animale (numero intero): ")
            try:
                peso = int(peso_input)
                break
            except ValueError:
                print("Errore nell'inserimento dei dati")
    
        # Ciclo while per assicurarsi che l'età sia un numero intero valido
        while True:
            eta_input = input("Inserisci l'età dell'animale (numero intero): ")
            try:
                eta = int(eta_input)
                break
            except ValueError:
                print("Errore nell'inserimento dei dati")

        # Inserisci i dati nel database
        sql = "INSERT INTO Mammiferi (nome, razza, peso, eta) VALUES ( %s, %s, %s, %s)"
        val = (nome, razza, peso, eta)
        mycursor.execute(sql, val)
        mydb.commit()
    case 2:
        #2) per visualizzare tutti gli animali
        mycursor.execute("SELECT * FROM Mammiferi")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
    case 3:
        #3)per eliminare un animale
        dede = input("inserisci l'id dell'animale da eliminare")
        sql = "DELETE FROM Mammiferi WHERE id = %s"
        val = (dede, )
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record eliminato.")

    case 4:
        #4)per modificare un animale"
        print("")
    case _:
        print("risposta errata")