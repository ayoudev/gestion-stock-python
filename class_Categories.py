import mysql.connector

class Categories:
    def __init__(self, id_categorie, nomCat):
        self.id_categorie = id_categorie
        self.nomCat = nomCat

    def ajouter(self):
        connexion = mysql.connector.connect(user='root', password='',
                                             host='localhost',
                                             database='')
        curseur = connexion.cursor()

        ajout_categorie = ("INSERT INTO Categories "
                           "(nomCat) "
                           "VALUES (%s)")
        valeur_categorie = (self.nomCat,)
        curseur.execute(ajout_categorie, valeur_categorie)

        # enregistrement de la modification
        connexion.commit()

        # fermeture de la connexion
        curseur.close()
        connexion.close()

    def modifier(self):
        connexion = mysql.connector.connect(user='root', password='',
                                             host='localhost',
                                             database='')
        curseur = connexion.cursor()

        maj_categorie = ("UPDATE Categories SET nomCat = %s WHERE id_categorie = %s")
        valeur_categorie = (self.nomCat, self.id_categorie)
        curseur.execute(maj_categorie, valeur_categorie)

        # enregistrement de la modification
        connexion.commit()

        # fermeture de la connexion
        curseur.close()
        connexion.close()

    def supprimer(self):
        connexion = mysql.connector.connect(user='root', password='',
                                             host='localhost',
                                             database='')
        curseur = connexion.cursor()

        supp_categorie = ("DELETE FROM Categories WHERE id_categorie = %s")
        valeur_categorie = (self.id_categorie,)
        curseur.execute(supp_categorie, valeur_categorie)

        # enregistrement de la modification
        connexion.commit()

        # fermeture de la connexion
        curseur.close()
        connexion.close()

    @staticmethod
    def afficher():
        connexion = mysql.connector.connect(user='root', password='',
                                             host='localhost',
                                             database='')
        curseur = connexion.cursor()

        affichage_categories = "SELECT * FROM Categories"
        curseur.execute(affichage_categories)

        # affichage des résultats
        for categorie in curseur:
            print(categorie)

        # fermeture de la connexion
        curseur.close()
        connexion.close()

    @staticmethod
    def chercher(nomCat):
        connexion = mysql.connector.connect(user='root', password='',
                                             host='localhost',
                                             database='')
        curseur = connexion.cursor()

        recherche_categorie = ("SELECT * FROM Categories WHERE nomCat LIKE %s")
        valeur_categorie = ('%' + nomCat + '%',)
        curseur.execute(recherche_categorie, valeur_categorie)

        # affichage des résultats
        for categorie in curseur:
            print(categorie)

        # fermeture de la connexion
        curseur.close()
        connexion.close()
