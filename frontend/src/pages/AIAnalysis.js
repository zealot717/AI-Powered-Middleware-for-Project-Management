// AIAnalysis.js - AI-based analysis of project risks and optimizations
/*import React from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import useFetch from "../hooks/useFetch";
import { API_BASE_URL } from "../services/api";
import AllocationChart from "../components/AllocationChart";

const AIAnalysis = () => {
  const { data: analysis, loading } = useFetch(`${API_BASE_URL}/ai-analysis`);

  if (loading) return <p>Loading AI analysis...</p>;

  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1 p-6">
        <Navbar />
        <h1 className="text-2xl font-bold mb-4">AI Analysis</h1>
        <h2 className="text-xl font-semibold">Optimized Resource Allocation</h2>
        <AllocationChart data={analysis.optimizedAllocations} />
        <h2 className="text-xl font-semibold mt-6">Predicted Risks</h2>
        <p>{analysis.riskPrediction}</p>
      </div>
    </div>
  );
};

export default AIAnalysis;*/
import React from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import useFetch from "../hooks/useFetch";
import { API_BASE_URL } from "../services/api";
import AllocationChart from "../components/AllocationChart";

const AIAnalysis = () => {
  const { data: analysis, loading, error } = useFetch(`${API_BASE_URL}/ai-analysis`);

  if (loading) return <p>Loading AI analysis...</p>;
  if (error) return <p>Error fetching AI analysis: {error.message}</p>;
  if (!analysis || !analysis.optimizedAllocations) return <p>No AI analysis data available.</p>;

  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1 p-6">
        <Navbar />
        <h1 className="text-2xl font-bold mb-4">AI Analysis</h1>
        <h2 className="text-xl font-semibold">Optimized Resource Allocation</h2>
        <AllocationChart data={analysis.optimizedAllocations || []} />
        <h2 className="text-xl font-semibold mt-6">Predicted Risks</h2>
        <p>{analysis.riskPrediction || "No risk predictions available."}</p>
      </div>
    </div>
  );
};

export default AIAnalysis;

