import mysql.connector

class Client:
    def __init__(self, id, nom, tel, mail, adresse, dateClient):
        self.id = id
        self.nom = nom
        self.tel = tel
        self.mail = mail
        self.adresse = adresse
        self.dateClient = dateClient

    def Ajouter(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database=""
        )
        cursor = conn.cursor()
        sql = "INSERT INTO clients (Nom, Tel, Mail, Adresse, DateClient) VALUES (%s, %s, %s, %s, %s)"
        val = (self.nom, self.tel, self.mail, self.adresse, self.dateClient)
        cursor.execute(sql, val)
        conn.commit()
        print(cursor.rowcount, "enregistrement ajouté avec succès.")

    def Modifier(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="",
            password="",
            database=""
        )
        cursor = conn.cursor()
        sql = "UPDATE clients SET Nom=%s, Tel=%s, Mail=%s, Adresse=%s, DateClient=%s WHERE ID=%s"
        val = (self.nom, self.tel, self.mail, self.adresse, self.dateClient, self.id)
        cursor.execute(sql, val)
        conn.commit()
        print(cursor.rowcount, "enregistrement mis à jour avec succès.")

    def supprimer(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="",
            password="",
            database=""
        )
        cursor = conn.cursor()
        sql = "DELETE FROM clients WHERE ID=%s"
        val = (self.id,)
        cursor.execute(sql, val)
        conn.commit()
        print(cursor.rowcount, "enregistrement(s) supprimé(s) avec succès.")

    def Afficher(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="yourdatabase"
        )
        cursor = conn.cursor()
        sql = "SELECT * FROM clients WHERE ID=%s"
        val = (self.id,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        return result

    def chercher(self, nom):
        conn = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="yourdatabase"
        )
        cursor = conn.cursor()
        sql = "SELECT * FROM clients WHERE Nom LIKE %s"
        val = ("%" + nom + "%",)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        for x in result:
            return x
