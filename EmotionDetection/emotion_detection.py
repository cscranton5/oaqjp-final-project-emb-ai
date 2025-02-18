import requests
import json


def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    INPUT = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(URL, headers = HEADERS, json = INPUT)

    data = json.loads(response.text)

    emotions = data['emotionPredictions'][0]['emotion']

    dominant_emotion = None
    for emotion in emotions:
        if dominant_emotion == None or emotions[emotion] > emotions[dominant_emotion]:
            dominant_emotion = emotion

    emotions['dominant_emotion'] = dominant_emotion

    return emotions