# Final project

Application web de détection d'émotions basée sur l'intelligence artificielle, développée dans le cadre du projet final du cours d'ingénierie logicielle Python / Flask (IBM Skills Network).

## 🚀 À propos du projet
Ce projet consiste à concevoir une application complète capable d'analyser le texte fourni par un utilisateur pour en extraire les scores de cinq émotions principales (`anger`, `disgust`, `fear`, `joy`, `sadness`) ainsi que l'émotion dominante. Le système intègre :
- Un module d'appel à l'API IBM Watson NLP.
- Un package Python structuré (`EmotionDetection`).
- Une suite de tests unitaires (`unittest`).
- Un serveur web de déploiement basé sur **Flask**.
- Une gestion robuste des erreurs (code HTTP 400 et entrées vides).
- Un code entièrement conforme aux standards de style **PEP 8** (Pylint 10/10).

## 📂 Structure du dépôt
```text
final_project/
│
├── EmotionDetection/
│   ├── __init__.py           # Package initialization
│   └── emotion_detection.py  # Logique d'appel à l'API Watson NLP
│
├── static/                   # Fichiers statiques (CSS, images)
├── templates/                # Templates HTML pour l'interface web
│
├── server.py                 # Application Flask principale
├── test_emotion_detection.py # Tests unitaires automatisés
└── README.md                 # Documentation du projet
```

## 🛠️ Technologies et Outils utilisés
- **Python 3.x**
- **Flask** (Framework web)
- **Requests** (Client HTTP pour l'API Watson NLP)
- **Unittest** (Tests unitaires)
- **Pylint** (Analyse de code statique)

## ⚙️ Installation et Utilisation (Environnement Skills Network Theia)

1. **Cloner le dépôt :**
   ```bash
   git clone <url-de-ton-depot-github>
   cd final_project
   ```

2. **Installer les dépendances :**
   ```bash
   pip3 install -r requirements.txt  # ou installation manuelle de Flask et Requests
   ```

3. **Exécuter les tests unitaires :**
   ```bash
   python3 -m unittest test_emotion_detection.py
   ```

4. **Lancer le serveur Flask :**
   ```bash
   python3 server.py
   ```
   L'application sera accessible localement sur le port `5000`.

## Auteur
Développé par un étudiant en Licence 2 Génie logiciel dans le cadre du parcours IBM Skills Network.
