from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    """Classe de tests unitaires pour le module de détection des émotions."""

    def test_emotion_detector(self):
        # Test pour la joie (joy)
        result_joy = emotion_detector("I am glad this happened")
        self.assertEqual(result_joy['dominant_emotion'], 'joy')

        # Test pour la colère (anger)
        result_anger = emotion_detector("I am really mad about this")
        self.assertEqual(result_anger['dominant_emotion'], 'anger')

        # Test pour le dégoût (disgust)
        result_disgust = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_disgust['dominant_emotion'], 'disgust')

        # Test pour la peur (fear)
        result_fear = emotion_detector("I am so afraid about this")
        self.assertEqual(result_fear['dominant_emotion'], 'fear')

        # Test pour la tristesse (sadness)
        result_sadness = emotion_detector("I am so sad about this")
        self.assertEqual(result_sadness['dominant_emotion'], 'sadness')

if __name__ == '__main__':
    unittest.main()