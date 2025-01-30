import React, { useState } from 'react';
import { predictDelay, allocateResources } from '../services/api';

const Dashboard = () => {
    const [result, setResult] = useState(null);

    const handlePrediction = async () => {
        const response = await predictDelay({ workers: 50, materials: 200 });
        setResult(response.data);
    };

    return (
        <div className="p-5">
            <h1 className="text-xl font-bold">Aerospace Project Dashboard</h1>
            <button onClick={handlePrediction} className="bg-blue-500 text-white p-2 rounded">
                Predict Delays
            </button>
            {result && <p>Predicted Delay: {result.predicted_delay}</p>}
        </div>
    );
};

export default Dashboard;