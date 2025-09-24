'''Application deployment script.'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_responder():
    '''Routing method for emotion detection application.

    Use input text to call emotion detection endpoint and return structured
    text response.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the result
    result = emotion_detector(text_to_analyze)
    dominant_emotion = result['dominant_emotion']

    # Check if dominant_emotion is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid input! Try again."

    # Remove dominant_emotion key to fit required return structure
    del result['dominant_emotion']

    # Return a formatted string with the sentiment label and score
    return f"For the given statement, the system response is {result}. The dominant emotion is  {dominant_emotion}."


@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
