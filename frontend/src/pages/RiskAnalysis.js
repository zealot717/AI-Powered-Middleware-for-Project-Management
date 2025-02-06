import React from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import useFetch from "../hooks/useFetch";

const RiskAnalysis = () => {
  const { data: risks, loading, error } = useFetch("/risk-analysis");

  if (loading) return <p className="text-gray-500">Loading risk analysis...</p>;
  if (error) return <p className="text-red-500">Error loading risks. Please try again.</p>;

  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1 p-6">
        <Navbar />
        <h1 className="text-2xl font-bold mb-4">Risk Analysis</h1>
        
        {risks && risks.length > 0 ? (
          <ul>
            {risks.map((risk, index) => (
              <li key={index} className="p-2 border-b">
                <strong>Project ID:</strong> {risk.project_id} <br />
                <strong>Risk Score:</strong> {risk.risk_score.toFixed(2)} <br />
                <strong>Risk Factors:</strong> {risk.risk_factors}
              </li>
            ))}
          </ul>
        ) : (
          <p className="text-gray-500">No risk data available.</p>
        )}
      </div>
    </div>
  );
};

export default RiskAnalysis;
