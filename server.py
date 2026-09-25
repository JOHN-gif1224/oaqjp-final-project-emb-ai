"""
Module de serveur Flask pour l'application de détection d'émotions.
Expose des points de terminaison web pour analyser le texte utilisateur.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialisation de l'application Flask
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """Analyse le texte de la requête GET et renvoie les scores d'émotion formatés."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Texte invalide ! Veuillez réessayer !"

    return (
        f"Pour le texte donné, la réponse est 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} et 'sadness': {response['sadness']}. "
        f"L'émotion dominante est **{response['dominant_emotion']}**."
    )

@app.route("/")
def render_index_html():
    """Rendu de la page d'accueil de l'application web."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)