import React from "react";
import useFetch from "../hooks/useFetch";
import AllocationChart from "../components/AllocationChart";

const AIAnalysis = () => {
  const { data: analysis, loading, error } = useFetch("/ai-analysis");

  if (loading) return <p className="text-gray-500">Loading AI analysis...</p>;
  if (error) return <p className="text-red-500">Error fetching AI analysis.</p>;

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-6">AI Analysis</h1>

      {/* Optimized Resource Allocation */}
      <h2 className="text-xl font-semibold">Optimized Resource Allocation</h2>
      {analysis.optimizedAllocations && analysis.optimizedAllocations.length > 0 ? (
        <AllocationChart data={analysis.optimizedAllocations} />
      ) : (
        <p className="text-gray-500">No AI allocation data available.</p>
      )}

      {/* Predicted Risks */}
      <h2 className="text-xl font-semibold mt-6">Predicted Risks</h2>
      <p>{analysis.riskPrediction || "No risk prediction available."}</p>
    </div>
  );
};

export default AIAnalysis;
