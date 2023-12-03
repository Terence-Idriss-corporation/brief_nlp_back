import psycopg2
import pandas as pd

import os
repertoire_de_travail = os.getcwd()
print("Répertoire de travail actuel :", repertoire_de_travail)

conn = psycopg2.connect(user="azAdmin", 
                       password="'ck}BNqnRsG5H?D", 
                       host="commentaires0database.postgres.database.azure.com", 
                       port=5432, 
                       database="postgres")

try:
    cursor = conn.cursor()
    cursor.execute("ROLLBACK")  # Effectuer un rollback pour nettoyer l'état de la transaction
    cursor.execute("SELECT * FROM nlp ORDER BY note DESC LIMIT 10;")
    nlp = cursor.fetchall()
except Exception as e:
    print(f"Une erreur est survenue : {e}")
    cursor.execute("ROLLBACK")  # Effectuer un rollback en cas d'erreur
    
cursor.close()
conn.close()


# Conversion des résultats en DataFrame
colonnes = [desc[0] for desc in cursor.description]
df = pd.DataFrame(nlp, columns=colonnes)

df.to_csv('src/data/best_films.csv', index=False, sep=";")
