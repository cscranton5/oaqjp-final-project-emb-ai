'''This the The server file for the application
 where we define the routes and start up there server'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This function calles the emotion_dtector function and returns its output'''

    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)

    if response['anger'] is None:
        return "Invalid text! Please try again!"

    return_text = f''' For the Given Statment, the system response is:
    'anger': {response['anger']}, 'disgust: {response['disgust']}, 'fear': {response['fear']}
    'joy': {response['joy']}, and 'sadness': {response['sadness']}. 
    The dominant emotion is {response['dominant_emotion']}.'''
    return return_text

@app.route("/")
def render_index_page():
    ''' This function renders the index file'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
