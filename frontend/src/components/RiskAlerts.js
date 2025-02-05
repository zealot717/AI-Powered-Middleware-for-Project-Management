import React, { useEffect, useState } from "react";
import { fetchRiskAnalysis } from "../services/api";

const RiskAlerts = () => {
    const [risks, setRisks] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const loadRisks = async () => {
            try {
                const data = await fetchRiskAnalysis();
                setRisks(data);
            } catch (err) {
                setError("Failed to fetch risk alerts");
            } finally {
                setLoading(false);
            }
        };

        loadRisks();
    }, []);

    if (loading) return <p>Loading risk alerts...</p>;
    if (error) return <p>{error}</p>;

    return (
        <div className="p-4">
            <h1 className="text-xl font-bold mb-4">Risk Alerts</h1>
            <ul className="space-y-3">
                {risks.map((risk, index) => (
                    <li key={index} className="p-2 bg-red-100 rounded">
                        <p><strong>{risk.ProjectID}</strong>: {risk.RiskLevel} Risk</p>
                        <p>{risk.Description}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default RiskAlerts;
