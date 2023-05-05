import mysql.connector

class Produits:
    def __init__(self, num, nom, description, prix_unitaire, quantite_en_stock, seuil_alerte_stock, date_derniere_entree_stock, date_derniere_sortie_stock, image, id_categorie):
        self.num = num
        self.nom = nom
        self.description = description
        self.prix_unitaire = prix_unitaire
        self.quantite_en_stock = quantite_en_stock
        self.seuil_alerte_stock = seuil_alerte_stock
        self.date_derniere_entree_stock = date_derniere_entree_stock
        self.date_derniere_sortie_stock = date_derniere_sortie_stock
        self.image = image
        self.id_categorie = id_categorie

    def ajouter(self):
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='PFA')
        cursor = cnx.cursor()
        ajout_produit = ("INSERT INTO produits "
                         "(num, nom, description, prix_unitaire, quantite_en_stock, seuil_alerte_stock, date_derniere_entree_stock, date_derniere_sortie_stock, image, id_categorie) "
                         "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        donnees_produit = (self.num, self.nom, self.description, self.prix_unitaire, self.quantite_en_stock, self.seuil_alerte_stock, self.date_derniere_entree_stock, self.date_derniere_sortie_stock, self.image, self.id_categorie)
        cursor.execute(ajout_produit, donnees_produit)
        cnx.commit()
        cursor.close()
        cnx.close()

    def modifier(self):
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='PFA')
        cursor = cnx.cursor()
        modification_produit = ("UPDATE produits "
                                "SET nom = %s, description = %s, prix_unitaire = %s, quantite_en_stock = %s, seuil_alerte_stock = %s, date_derniere_entree_stock = %s, date_derniere_sortie_stock = %s, image = %s, id_categorie = %s "
                                "WHERE num = %s")
        donnees_produit = (self.nom, self.description, self.prix_unitaire, self.quantite_en_stock, self.seuil_alerte_stock, self.date_derniere_entree_stock, self.date_derniere_sortie_stock, self.image, self.id_categorie, self.num)
        cursor.execute(modification_produit, donnees_produit)
        cnx.commit()
        cursor.close()
        cnx.close()

    def supprimer(self):
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='PFA')
        cursor = cnx.cursor()
        suppression_produit = ("DELETE FROM produits "
                               "WHERE num = %s")
        donnees_produit = (self.num,)
        cursor.execute(suppression_produit, donnees_produit)
        cnx.commit()
        cursor.close()
        cnx.close()

    @staticmethod
    def afficher(nom_produit):
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='PFA')
        cursor = cnx.cursor()
        requete_produit = ("SELECT * FROM produits "
                           "WHERE nom = %s")
        donnees_produit = (nom_produit,)
        cursor.execute(requete_produit, donnees_produit)
        resultat = cursor.fetchone()
        if resultat is not None:
            num, nom, description, prix_unitaire, quantite_en_stock, seuil_alerte_stock, date_derniere_entree_stock, date_derniere_sortie_stock, id_categorie, image = resultat
            produit = Produits(num, nom, description, prix_unitaire, quantite_en_stock, seuil_alerte_stock,
                               date_derniere_entree_stock, date_derniere_sortie_stock, id_categorie, image)
            return produit
        else:
            return None
        cursor.close()
        cnx.close()

#method_Recherche
        def rechercher_par_critere(critere, valeur):
            cnx = mysql.connector.connect(user='root', password='', host='localhost',
                                          database='PFA')
            cursor = cnx.cursor()
            if critere == 'nom':
                requete_produits = ("SELECT * FROM produits "
                                    "WHERE nom LIKE %s")
                valeur_recherche = ('%' + valeur + '%',)
            elif critere == 'prix_unitaire':
                requete_produits = ("SELECT * FROM produits "
                                    "WHERE prix_unitaire <= %s")
                valeur_recherche = (valeur,)
            elif critere == 'quantite':
                requete_produits = ("SELECT * FROM produits "
                                    "WHERE quantite_en_stock <= %s")
                valeur_recherche = (valeur,)
            elif critere == 'date_entree':
                requete_produits = ("SELECT * FROM produits "
                                    "WHERE date_derniere_entree_stock <= %s")
                valeur_recherche = (valeur,)
#chercher avec categorie
            elif critere == 'categorie':
                requete_produits = ("SELECT * FROM produits JOIN Categories "
                                    "WHERE produits.id_categorie = Categories.id_categorie AND nom_Cat LIKE %s")
                valeur_recherche = ('%' + valeur + '%',)

            else:
                return None

            cursor.execute(requete_produits, valeur_recherche)
            resultats = []
            for resultat in cursor:
                num, nom, description, prix_unitaire, quantite_en_stock, seuil_alerte_stock, date_derniere_entree_stock, date_derniere_sortie_stock, image = resultat
                produit = Produits(num, nom, description, prix_unitaire, quantite_en_stock, seuil_alerte_stock,
                                   date_derniere_entree_stock, date_derniere_sortie_stock, image)
                resultats.append(produit)

            cursor.close()
            cnx.close()

            return resultats
