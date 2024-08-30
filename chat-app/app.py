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

# Mapping sentiment to emoji and color
SENTIMENT_MAP = {
    'positive': {'emoji': '😊', 'color': '#a8e6cf'},  # Light green
    'neutral': {'emoji': '😐', 'color': '#ffd3b6'},   # Light orange
    'negative': {'emoji': '😞', 'color': '#ff8b94'},  # Light red
}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg)
    
    # Perform sentiment analysis
    sentiment_score = sentiment_analyzer.polarity_scores(msg)
    if sentiment_score['compound'] >= 0.05:
        sentiment = 'positive'
    elif sentiment_score['compound'] <= -0.05:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    
    emoji = SENTIMENT_MAP[sentiment]['emoji']
    color = SENTIMENT_MAP[sentiment]['color']
    
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

        # Send the AI message, emoji, and color back to the client
        send({"text": ai_message, "emoji": emoji, "color": color, "sentiment": sentiment}, broadcast=True)
        
    except Exception as e:
        print(f"Error communicating with Groq API: {e}")
        send({"text": "Sorry, there was an error processing your request.", "emoji": "😕", "color": "#cccccc"}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
