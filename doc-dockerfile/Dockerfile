#FROM ubuntu:latest

#RUN apt-get update && \
   # apt-get install -y nginx ssh nano iputils-ping && \
   # apt-get clean

#EXPOSE 80

#CMD ["nginx", "-g", "daemon off;"]

# Utiliser l'image Python comme image de base
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt et installer les dépendances
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers de l'application
COPY . .

# Exposer le port que l'application utilisera
EXPOSE 5000

# Commande par défaut pour exécuter l'application
CMD ["python", "app.py"]

