import mysql.connector

class Client:
    def __init__(self, prenom="", nom="", tel="", mail="", adresse="", dateN=""):
        self.prenom=prenom
        self.nom = nom
        self.tel = tel
        self.mail = mail
        self.adresse = adresse
        self.dateN = dateN 


    def Ajouter(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pfa"
        )
        cursor = conn.cursor()
        sql = "INSERT INTO client (nom, prenom, tel, mail, adresse, dateN) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (self.nom, self.prenom, self.tel, self.mail, self.adresse, self.dateN)
        cursor.execute(sql, val)
        conn.commit()
        print(cursor.rowcount, "enregistrement ajouté avec succès.")

    def Modifier(self, ID):
        sql = "UPDATE client SET prenom=%s, nom=%s, tel=%s, mail=%s, adresse=%s, dateN=%s WHERE idC=%s"
        val = (self.prenom, self.nom, self.tel, self.mail, self.adresse, self.dateN, ID)
        return sql, val

    def supprimer(self, ID):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pfa"
            )
        cursor = conn.cursor()
        sql = "DELETE FROM client WHERE idC=%s"
        val = (ID,)
        cursor.execute(sql, val)
        conn.commit()
        print(cursor.rowcount, "enregistrement(s) supprimé(s) avec succès.")


