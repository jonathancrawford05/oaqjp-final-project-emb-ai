import requests

def emotion_detector(text_to_analyze: str)->str:
    '''Get response text from the emotion detection model API endpoint

    Args:
        text_to_analyze (str): Input text to be sent for emotion detection

    Outputs:
        (str): response objects text attribute's value
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, json = myobj, headers=header)

    return response.text
