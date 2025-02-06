/*import React from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import useFetch from "../hooks/useFetch";
import { API_BASE_URL } from "../services/api";
import RiskCard from "../components/RiskCard";

const RiskAnalysis = () => {
  const { data: risks, loading } = useFetch(`${API_BASE_URL}/risk-analysis`);

  if (loading) return <p>Loading risk analysis...</p>;

  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1 p-6">
        <Navbar />
        <h1 className="text-2xl font-bold mb-4">Risk Analysis</h1>
        <div className="grid grid-cols-3 gap-4">
          {risks.map((risk) => (
            <RiskCard key={risk.id} project={risk} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default RiskAnalysis;
*/

import React from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import useFetch from "../hooks/useFetch";
import { API_BASE_URL } from "../services/api";

const RiskAnalysis = () => {
  const { data, loading, error } = useFetch(`${API_BASE_URL}/risk-analysis`);

  if (loading) return <p>Loading risk analysis...</p>;
  if (error) return <p>Error loading risk analysis.</p>;
  if (!data || !Array.isArray(data.risks)) return <p>No risk data available.</p>; // Fixes `.map()` error

  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1 p-6">
        <Navbar />
        <h1 className="text-2xl font-bold mb-4">Risk Analysis</h1>
        <h2 className="text-xl font-semibold">Risk Factors</h2>
        <ul>
          {data.risks.map((risk, index) => (
            <li key={index} className="p-2 bg-gray-100 mb-2 rounded">{risk}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default RiskAnalysis;
