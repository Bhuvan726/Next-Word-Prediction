from flask import Flask, request, jsonify
import sqlite3
import random

app = Flask(__name__)

# Connect to SQLite Database
def init_db():
    conn = sqlite3.connect('predictions.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS predictions (id INTEGER PRIMARY KEY, word TEXT)''')
    conn.commit()
    conn.close()

init_db()

# Sample word prediction
words = ["hello", "world", "how", "are", "you"]

@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.json.get('text', '')
    next_word = random.choice(words)  # Replace with your model prediction logic
 
    
    # Insert the prediction into the database
    conn = sqlite3.connect('predictions.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO predictions (word) VALUES (?)", (next_word,))
    conn.commit()
    conn.close()
    
    return jsonify({"next_word": next_word})

    return jsonify({"next_word": next_word})

if __name__ == '__main__':
    app.run(debug=True)
