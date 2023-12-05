# Sommaire du backend

1. [Création de l'environnement virtuel](#1-création-de-lenvironnement-virtuel)
    - [Activation de l'environnement virtuel](#activation-de-lenvironnement-virtuel)
    - [Désactivation de l'environnement virtuel](#désactivation-de-lenvironnement-virtuel)

2. [Installation des dépendances](#2-installation-des-dc3a9pendances-1)
___

### 1. Création de l'environnement virtuel
Utilisez la commande suivante après avoir ouvert le terminal de votre éditeur de code
```
py -m venv .venv
```
### Activation de l'environnement virtuel (Obligatoire pour les installations et le lancement du serveur)
- Avec CMD (Command Prompt)
    ```
    .venv\Scripts\activate.bat   
    ```
- Avec Powershell
    ```
    .venv\Scripts\activate 
    ```
___
### Désactivation de l'environnement virtuel
- Avec CMD (Command Prompt)
    ```
    .venv\Scripts\deactivate.bat   
    ```
- Avec Powershell
    ```
    deactivate
    ```
___
### 2. Installation des dépendances
```
pip install -r requirements.txt
```
___
### 3. Lancer le serveur django
```
cd src
py manage.py runserver
```
