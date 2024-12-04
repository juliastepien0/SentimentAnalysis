''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from SentAnalysis.sent_analysis import sentiment_analyzer
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    try:
        text_to_analyze = request.args.get("textToAnalyze")
        if not text_to_analyze or len(text_to_analyze) < 20:
            return "The text you provided is too short, please enter valid text.", 400

        response = sentiment_analyzer(text_to_analyze)
        if not response or "label" not in response or "score" not in response:
            return "Unexpected error occurred. Please check the text provided.", 500

        label = response.get("label")
        score = response.get("score")
        return f"The given text has been identified as {label} and its score is {score}.", 200

    except Exception as e:
        return "Something bad occurred"

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug = True)
