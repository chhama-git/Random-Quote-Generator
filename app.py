from flask import Flask, render_template
import random

app = Flask(__name__)

# List of motivational quotes
quotes = [
    "Believe in yourself!",
    "Stay positive, work hard, make it happen.",
    "Success is the sum of small efforts repeated day in and day out.",
    "Dream big and dare to fail.",
    "Don’t watch the clock; do what it does. Keep going."
]

@app.route('/')
def home():
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
