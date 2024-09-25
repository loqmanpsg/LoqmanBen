from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os

# Créer une instance de FastAPI
app = FastAPI()

# Configurer la connexion à la base de données PostgreSQL
DATABASE_URL = 'postgresql://postgres:P@ssw0rd@172.0.0.1/db'  # Utilisez 172.0.0.1 comme adresse IP
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Route pour servir le favicon
@app.get("/favicon.ico")
async def get_favicon():
    return FileResponse(os.path.join("static", "favicon.ico"))

# Route principale pour récupérer les informations des clients
@app.get('/')
def read_root():
    # Créer une session de base de données
    session = Session()
    try:
        # Exécuter la requête SQL pour récupérer les informations des clients
        result = session.execute(text('SELECT customer_id, company_name, contact_name FROM customers'))
        # Convertir les résultats en une liste de dictionnaires
        customers_info = [dict(customerid=row[0], companyname=row[1], contactname=row[2]) for row in result]
        return {'Customers info': customers_info}
    except Exception as e:
        # Gérer les exceptions et renvoyer une erreur HTTP
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Fermer la session pour éviter les fuites de ressources
        session.close()

# Exemple de point de terminaison supplémentaire (optionnel)
@app.get("/health")
def health_check():
    return {"status": "ok"}
