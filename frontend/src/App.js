import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [time, setTime] = useState('');
    const [resources, setResources] = useState('');
    const [prediction, setPrediction] = useState(null);

    const handlePredict = async () => {
        try {
            const response = await axios.post('http://127.0.0.1:8000/predict_cost', {
                time: parseFloat(time),
                resources: parseFloat(resources)
            });
            setPrediction(response.data.predicted_cost);
        } catch (error) {
            console.error("Error fetching prediction:", error);
        }
    };

    return (
        <div>
            <h1>AI-Powered Project Cost Predictor</h1>
            <input type="number" placeholder="Time (weeks)" value={time} onChange={(e) => setTime(e.target.value)} />
            <input type="number" placeholder="Resources" value={resources} onChange={(e) => setResources(e.target.value)} />
            <button onClick={handlePredict}>Predict Cost</button>
            {prediction && <h2>Estimated Cost: ${prediction}</h2>}
        </div>
    );
}

export default App;