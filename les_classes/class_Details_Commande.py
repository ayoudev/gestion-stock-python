import mysql.connector

class Details_Commande:
    
    def __init__(self, IDcommande="", datecommand="", nomClient="", produit="", QtiteProd="", Remise="", TVA="", TOTAL_TH="", TOTAL_TTC=""):
        
        self.IDcommande = IDcommande
        self.datecommand = datecommand
        self.nomClient = nomClient
        self.produit = produit
        self.QtiteProd = QtiteProd 
        self.Remise = Remise
        self.TVA = TVA
        self.TOTAL_TH = TOTAL_TH
        self.TOTAL_TTC = TOTAL_TTC
        
        
    
    def Ajouter(self):
        # se connecter à la base de données
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pfa"
        )
        mycursor = mydb.cursor()
        
        # insérer une nouvelle commande dans la table Details_Commande
        sql = "INSERT INTO details_commande (IDcommande, datecommand, nomClient, produit, QtiteProd, Remise, TVA, TOTAL_TH, TOTAL_TTC) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (self.IDcommande, self.datecommand, self.nomClient, self.produit, self.QtiteProd, self.Remise, self.TVA, self.TOTAL_TH, self.TOTAL_TTC)
        mycursor.execute(sql, values)
        mydb.commit()
        print(mycursor.rowcount, "détails de commande ajoutés.")


    def Modifier(self):
        # se connecter à la base de données
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pfa"
        )
        mycursor = mydb.cursor() 
        # mettre à jour les informations de la commande dans la base de données
        sql = "UPDATE details_commande SET datecommand = %s, nomClient = %s, produit = %s, QtiteProd = %s, Remise = %s, TVA = %s, TOTAL_TH = %s, TOTAL_TTC = %s WHERE IDcommande = %s"
        values = (self.datecommand, self.nomClient, self.produit, self.QtiteProd, self.Remise, self.TVA, self.TOTAL_TH, self.TOTAL_TTC, self.IDcommande)
        mycursor.execute(sql, values)
        mydb.commit()
        print(mycursor.rowcount, "détails de commande modifiés.")   

    def Supprimer(self, IDcommande):
        # se connecter à la base de données
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pfa"
        )
        mycursor = mydb.cursor()
        # supprimer la commande de la base de données
        sql = "DELETE FROM details_commande WHERE IDcommande = %s"
        mycursor.execute(sql, (IDcommande,))
        mydb.commit()
        print(mycursor.rowcount, "détails de commande supprimés.")    
    
    def Afficher(self):
        # se connecter à la base de données
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pfa"
        )
        mycursor = mydb.cursor()
        
        # afficher les détails de commande avec l'IDcommande donné
        sql = "SELECT * FROM details_commande WHERE IDcommande = %s"
        value = (self.IDcommande,)
        mycursor.execute(sql, value)
        myresult = mycursor.fetchall()
        for x in myresult:
            return x
    

