
class EmotionsRepository:

    def __init__(self):
        self._emotions = [
            'sadness',
            'neutral',
            'disgust',
            'anger',
            'surprise',
            'fear',
            'happiness'
        ]

    def get_emotions(self):
        return self._emotions
