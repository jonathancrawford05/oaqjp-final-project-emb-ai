import requests
import json

def emotion_detector(text_to_analyze: str)->str:
    '''Extract emotions with scores from the emotion detection model API endpoint.

    Use input text to call emotion detection endpoint and return a dictionary
    containing the emotions as keys and scores as values.

    Args:
        text_to_analyze (str): Input text to be sent for emotion detection

    Outputs:
        (dict): Dictionary with emotions and their score the
                last key value pair highlights top scoring emotion
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, json = myobj, headers=header)
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    # Extracting emotions labels and scores from the response
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    # Extract the top scoring (dominant) emotion
    dominant_emotion = max(emotions, key=emotions.get)
    # Add the dominant emotion to the return dict.
    emotions.update({'dominant_emotion': dominant_emotion})

    return emotions
