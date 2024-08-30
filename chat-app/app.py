import os
from flask import Flask, render_template
from flask_socketio import SocketIO, send
from groq import Groq
from dotenv import load_dotenv
from nltk.sentiment.vader import SentimentIntensityAnalyzer

load_dotenv()

app = Flask(__name__)
socketio = SocketIO(app)

if not os.environ.get("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Initialize the sentiment analyzer
sentiment_analyzer = SentimentIntensityAnalyzer()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg)
    
    # Perform sentiment analysis
    sentiment_score = sentiment_analyzer.polarity_scores(msg)
    sentiment = max(sentiment_score, key=sentiment_score.get)
    print(f"Sentiment: {sentiment}, Scores: {sentiment_score}")

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": msg,
                }
            ],
            model="llama3-8b-8192",
        )

        ai_message = chat_completion.choices[0].message.content

        # Send both the AI message and the sentiment analysis result
        send({"text": ai_message, "sentiment": sentiment}, broadcast=True)
        
    except Exception as e:
        print(f"Error communicating with Groq API: {e}")
        send("Sorry, there was an error processing your request.", broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
