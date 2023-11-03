# Utiliser une image Python officielle
FROM python:3.11

# Définir l'environnement de travail dans le conteneur
WORKDIR /app

# Ajouter les fichiers de dépendances
ADD requirements.txt .

# Installer les dépendances
RUN pip install -r requirements.txt

# Copier le reste du code de l'application
RUN mkdir ./src
COPY ./src ./src

# Ajouter un volume pour le dossier src
VOLUME /app/src

# Exposer le port sur lequel l'application s'exécute
EXPOSE 8000

# Définir la commande pour exécuter l'application
CMD ["python", "/app/src/manage.py", "runserver --settings=src.settings_deployment", "0.0.0.0:8000"]