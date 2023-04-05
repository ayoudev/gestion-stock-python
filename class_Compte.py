import mysql.connector


class Compte:
    def __init__(self, nom_utilisateur, mot_de_passe):
        self.nom_utilisateur = nom_utilisateur
        self.mot_de_passe = mot_de_passe

    # autres méthodes de la classe

    @staticmethod
    def verifier_compte(nom_utilisateur, mot_de_passe):
        cnx = mysql.connector.connect(user='root', password='', host='localhost',
                                      database='')
        cursor = cnx.cursor()

        requete_verification = ("SELECT id FROM comptes "
                                "WHERE nom_utilisateur = %s AND mot_de_passe = %s")
        donnees = (nom_utilisateur, mot_de_passe)

        cursor.execute(requete_verification, donnees)
        compte_existe = cursor.fetchone() is not None

        cursor.close()
        cnx.close()

        return compte_existe

    @staticmethod
    def ajouter(nom_utilisateur, mot_de_passe):
        cnx = mysql.connector.connect(user='root', password='', host='localhost',
                                      database='')
        cursor = cnx.cursor()

        requete_ajout = ("INSERT INTO comptes (nom_utilisateur, mot_de_passe) "
                         "VALUES (%s, %s)")
        donnees = (nom_utilisateur, mot_de_passe)

        cursor.execute(requete_ajout, donnees)
        cnx.commit()

        id_compte = cursor.lastrowid

        cursor.close()
        cnx.close()

        return id_compte

    @staticmethod
    def modifier(id_compte, nom_utilisateur, mot_de_passe):
        cnx = mysql.connector.connect(user='root', password='motdepasse', host='localhost',
                                      database='ma_base_de_donnees')
        cursor = cnx.cursor()

        requete_modification = ("UPDATE comptes SET nom_utilisateur = %s, mot_de_passe = %s "
                                "WHERE id = %s")
        donnees = (nom_utilisateur, mot_de_passe, id_compte)

        cursor.execute(requete_modification, donnees)
        cnx.commit()

        cursor.close()
        cnx.close()

    @staticmethod
    def supprimer(id_compte):
        cnx = mysql.connector.connect(user='root', password='motdepasse', host='localhost',
                                      database='ma_base_de_donnees')
        cursor = cnx.cursor()

        requete_suppression = ("DELETE FROM comptes "
                               "WHERE id = %s")
        donnees = (id_compte,)

        cursor.execute(requete_suppression, donnees)
        cnx.commit()

        cursor.close()
        cnx.close()
