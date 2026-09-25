import requests
import json

def emotion_detector(text_to_analyze):
    """
    Envoie un texte à l'API Watson NLP Emotion Predict, extrait les scores
    des 5 émotions principales et détermine l'émotion dominante.

    Paramètre :
        text_to_analyze (str) : le texte client à analyser

    Retour :
        dict : {
            'anger': float, 'disgust': float, 'fear': float,
            'joy': float, 'sadness': float,
            'dominant_emotion': str
        }
    """
    # Gestion des entrées vides ou invalides (Correction Tâche 7)
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=myobj, headers=headers)

    # Gestion du code d'état HTTP 400 (Bad Request renvoyé par l'API)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Étape 1 : convertir la chaîne JSON (str) en dictionnaire Python
    formatted_response = json.loads(response.text)

    # Étape 2 : naviguer dans la structure imbriquée pour atteindre les scores
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Étape 3 : extraire chaque score individuellement
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # Étape 4 : déterminer l'émotion dominante = celle qui a le score le plus élevé
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Étape 5 : construire le dictionnaire de sortie attendu par le projet
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }