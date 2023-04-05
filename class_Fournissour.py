import mysql.connector

class Fournisseur:
    def __init__(self, CodePostalFornisseur, NomFornisseur, VilleFornisseur, TeleFornisseur, EmailFornisseur, AdresseFornisseur):
        self.CodePostalFornisseur = CodePostalFornisseur
        self.NomFornisseur = NomFornisseur
        self.VilleFornisseur = VilleFornisseur
        self.TeleFornisseur = TeleFornisseur
        self.EmailFornisseur = EmailFornisseur
        self.AdresseFornisseur = AdresseFornisseur
        self.conn = mysql.connector.connect(host='localhost',
                                            database='',
                                            user='root',
                                            password='')
        self.cursor = self.conn.cursor()

    def Ajouter(self):
        sql = "INSERT INTO Fournisseurs (CodePostalFornisseur, NomFornisseur, VilleFornisseur, TeleFornisseur, EmailFornisseur, AdresseFornisseur) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (self.CodePostalFornisseur, self.NomFornisseur, self.VilleFornisseur, self.TeleFornisseur, self.EmailFornisseur, self.AdresseFornisseur)
        self.cursor.execute(sql, values)
        self.conn.commit()
        print(self.cursor.rowcount, "Fournisseur ajouté avec succès")

    def Modifier(self, CodePostalFornisseur):
        sql = "UPDATE Fournisseurs SET NomFornisseur=%s, VilleFornisseur=%s, TeleFornisseur=%s, EmailFornisseur=%s, AdresseFornisseur=%s WHERE CodePostalFornisseur=%s"
        values = (self.NomFornisseur, self.VilleFornisseur, self.TeleFornisseur, self.EmailFornisseur, self.AdresseFornisseur, CodePostalFornisseur)
        self.cursor.execute(sql, values)
        self.conn.commit()
        print(self.cursor.rowcount, "Fournisseur modifié avec succès")

    def Supprimer(self, CodePostalFornisseur):
        sql = "DELETE FROM Fournisseurs WHERE CodePostalFornisseur=%s"
        values = (CodePostalFornisseur,)
        self.cursor.execute(sql, values)
        self.conn.commit()
        print(self.cursor.rowcount, "Fournisseur supprimé avec succès")

    def Afficher(self):
        sql = "SELECT * FROM Fournisseurs"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            return row

    def Chercher(self, NomFornisseur):
        sql = "SELECT * FROM Fournisseurs WHERE NomFornisseur LIKE %s"
        values = ('%' + NomFornisseur + '%',)
        self.cursor.execute(sql, values)
        result = self.cursor.fetchall()
        for row in result:
            return row
