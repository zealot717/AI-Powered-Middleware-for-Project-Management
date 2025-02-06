import React from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import useFetch from "../hooks/useFetch";
import AllocationChart from "../components/AllocationChart";

const Allocations = () => {
  const { data: allocations, loading, error } = useFetch("/allocations");

  if (loading) return <p className="text-gray-500">Loading allocations...</p>;
  if (error) return <p className="text-red-500">Error loading allocations. Please try again.</p>;

  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1 p-6">
        <Navbar />
        <h1 className="text-2xl font-bold mb-4">Resource Allocations</h1>

        {allocations.length > 0 ? (
          <ul>
            {allocations.map((alloc, index) => (
              <li key={index} className="p-2 border-b">
                <strong>Task ID:</strong> {alloc.TaskID} <br />
                <strong>Assigned Resource:</strong> {alloc.AssignedResource}
              </li>
            ))}
          </ul>
        ) : (
          <p className="text-gray-500">No allocation data available.</p>
        )}

        {/* Visualization */}
        {allocations.length > 0 && <AllocationChart data={allocations} />}
      </div>
    </div>
  );
};

export default Allocations;
