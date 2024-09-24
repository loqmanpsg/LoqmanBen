FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application dans le conteneur
COPY ./app /app

# Installer les dépendances à partir de requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Commande à exécuter lorsque le conteneur démarre
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
