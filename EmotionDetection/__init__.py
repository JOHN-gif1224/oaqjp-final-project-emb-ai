"""
Fichier d'initialisation du package EmotionDetection.

Ce fichier indique à Python que le dossier EmotionDetection
doit être traité comme un package importable, et expose
directement la fonction emotion_detector au niveau du package.
"""

# Import relatif : on va chercher emotion_detector dans le module
# emotion_detection.py situé dans CE MÊME package (d'où le point ".")
from .emotion_detection import emotion_detector