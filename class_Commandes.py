import mysql.connector

class Commande:
    def __init__(self, IDcommande, DateCommande, idClient, Total_HT, TVA, TOTAL_TTC):
        self.IDcommande = IDcommande
        self.DateCommande = DateCommande
        self.idClient = idClient
        self.Total_HT = Total_HT
        self.TVA = TVA
        self.TOTAL_TTC = TOTAL_TTC

    def Ajouter(self):
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='PFA')
        cursor = conn.cursor()
        sql = "INSERT INTO Commandes (IDcommande, DateCommande, idClient, Total_HT, TVA, TOTAL_TTC) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (self.IDcommande, self.DateCommande, self.idClient, self.Total_HT, self.TVA, self.TOTAL_TTC)
        cursor.execute(sql, val)
        conn.commit()
        print(cursor.rowcount, "enregistrement ajouté")

    def Afficher(self):
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='PFA')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Commandes WHERE IDcommande = {}".format(self.IDcommande))
        result = cursor.fetchone()
        return result

    def chercher(self, dateCommande):
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='PFA')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Commandes WHERE DateCommande = '{}'".format(dateCommande))
        result = cursor.fetchall()
        for row in result:
           return row
