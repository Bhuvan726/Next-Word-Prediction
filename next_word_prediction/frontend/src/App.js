import React, { useState } from 'react';

function App() {
    const [text, setText] = useState('');
    const [prediction, setPrediction] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await fetch('http://localhost:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text }),
        });
        const data = await response.json();
        setPrediction(data.next_word);
    };

    return (
        <div>
            <h1>Next Word Prediction</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                    placeholder="Type a word"
                />
                <button type="submit">Predict Next Word</button>
            </form>
            {prediction && <h2>Predicted Next Word: {prediction}</h2>}
        </div>
    );
}

export default App;
