import mysql.connector
from mysql.connector import Error
####
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QDialog, QApplication, QMessageBox
#from ..signup import *
####
import bcrypt
import base64, hashlib
class Compte:
   

    def __init__(self, nom_utilisateur, mdp):
        self.nom_utilisateur = nom_utilisateur
        self.mdp = mdp
        

     # Méthode pour vérifier si le compte existe dans la base de données MySQL
    def verifier_compte(self):
        # Connexion à la base de données
        try:
            mydb = mysql.connector.connect(
                                        host='localhost',
                                           database='pfa',
                                           user='root',
                                           password='')

        # Exécution de la requête SQL pour récupérer le compte correspondant au nom d'utilisateur et au mot de passe
            mycursor = mydb.cursor()
            sql = "SELECT * FROM compte WHERE nom_utilisateur = %s AND mdp = %s"
            val = (self.nom_utilisateur, self.mdp)
            mycursor.execute(sql, val)
        
            # Vérification du résultat de la requête
            result = mycursor.fetchone()
            if result:
                return True  # le compte existe dans la base de données
            else:
                return False  # le compte n'existe pas dans la base de données
        except:
            print("error")
    

    
    def ajouter(self):
        
        ## verifier si le compte est deja existe
        compte = Compte( self.nom_utilisateur,self.mdp)
        ct_v=compte.verifier_compte()
        
        if ct_v==True:
            return 0
             
        else:
            password=self.mdp.encode('utf-8')
            hash_pass = bcrypt.hashpw(base64.b64encode(hashlib.sha256(password).digest()),bcrypt.gensalt())
             
            try:
                conn = mysql.connector.connect(host='localhost',
                                           database='pfa',
                                           user='root',
                                           password='')
                cursor = conn.cursor()
                cursor.execute("INSERT INTO compte (nom_utilisateur, mdp) VALUES (%s, %s)", 
                           (self.nom_utilisateur, hash_pass))
                conn.commit()
                return 1
            except Error as e:
                print(e)
                return None
            finally:
                cursor.close()
                conn.close()

    def modifier(self):
        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='pfa',
                                           user='root',
                                           password='')
            cursor = conn.cursor()
            cursor.execute("UPDATE compte SET mdp = %s WHERE nom_utilisateur = %s", 
                           (self.mdp, self.nom_utilisateur))
            conn.commit()
            print("Compte modifié avec succès !")
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def supprimer(self):
        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='pfa',
                                           user='root',
                                           password='')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM compte WHERE nom_utilisateur = %s", (self.nom_utilisateur,))
            conn.commit()
            print("Compte supprimé avec succès !")
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()