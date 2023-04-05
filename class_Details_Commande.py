import mysql.connector

class Details_Commande:
    
    def __init__(self, IdDetail, IDcommande, IDProduit, NomProduit, Quantite, Prix, Remise, TOTal, datecommand):
        self.IdDetail = IdDetail
        self.IDcommande = IDcommande
        self.IDProduit = IDProduit
        self.NomProduit = NomProduit
        self.Quantite = Quantite
        self.Prix = Prix
        self.Remise = Remise
        self.TOTal = TOTal
        self.datecommand = datecommand
    
    def Ajouter(self):
        # se connecter à la base de données
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="PFA"
        )
        mycursor = mydb.cursor()
        
        # insérer une nouvelle commande dans la table Details_Commande
        sql = "INSERT INTO Details_Commande (IdDetail, IDcommande, IDProduit, NomProduit, Quantite, Prix, Remise, TOTal, datecommand) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (self.IdDetail, self.IDcommande, self.IDProduit, self.NomProduit, self.Quantite, self.Prix, self.Remise, self.TOTal, self.datecommand)
        mycursor.execute(sql, values)
        mydb.commit()
        print(mycursor.rowcount, "détails de commande ajoutés.")
    
    def Afficher(self):
        # se connecter à la base de données
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="PFA"
        )
        mycursor = mydb.cursor()
        
        # afficher les détails de commande avec l'IDcommande donné
        sql = "SELECT * FROM Details_Commande WHERE IDcommande = %s"
        value = (self.IDcommande,)
        mycursor.execute(sql, value)
        myresult = mycursor.fetchall()
        for x in myresult:
            return x
    
    def chercher(self, date):
        # se connecter à la base de données
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="PFA"
        )
        mycursor = mydb.cursor()
        
        # chercher les détails de commande avec la date donnée
        sql = "SELECT * FROM Details_Commande WHERE datecommand = %s"
        value = (date,)
        mycursor.execute(sql, value)
        myresult = mycursor.fetchall()
        for x in myresult:
            return x
