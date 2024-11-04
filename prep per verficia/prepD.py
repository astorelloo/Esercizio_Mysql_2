import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "Animali"
)
mycursor = mydb.cursor()

# Chiede all'utente se vuole inserire un nuovo animale, per un totale di 5 volte
risp = input("vuoi inserire altri 5 animali?(Y o N)")
if risp == "Y" or risp=="y":
    for i in range(5):
        print(f"Inserimento animale {i+1} di 5:")
        nome = input("Inserisci il nome dell'animale: ")
        razza = input("Inserisci la razza dell'animale: ")
        # Verifica se il peso è un intero
        
        while True:
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
    # Conferma le modifiche al database
    mydb.commit()
else:
    print("non hai voluto inserire alcun animale")